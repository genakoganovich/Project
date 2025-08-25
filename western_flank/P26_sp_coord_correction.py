import math
import re
import sys
from pathlib import Path
from glob import glob


# -------------------- parsing & helpers --------------------

def parse_line(line: str):
    parts = line.split()
    if len(parts) < 6:
        return None
    try:
        value = float(parts[1])
        x = int(parts[-3])
        y = int(parts[-2])
    except ValueError:
        return None
    return line.rstrip("\n"), value, x, y


def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def regression_angle(values, xs, ys):
    n = len(values)
    v_mean = sum(values) / n
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n

    denom = sum((v - v_mean) ** 2 for v in values)
    if denom == 0:
        dx = xs[-1] - xs[0]
        dy = ys[-1] - ys[0]
        return math.atan2(dy, dx)

    dx_dv = sum((v - v_mean) * (x - x_mean) for v, x in zip(values, xs)) / denom
    dy_dv = sum((v - v_mean) * (y - y_mean) for v, y in zip(values, ys)) / denom
    return math.atan2(dy_dv, dx_dv)


def shift_point(x, y, angle, shift):
    dx = math.cos(angle) * shift
    dy = math.sin(angle) * shift
    return int(round(x + dx)), int(round(y + dy))


_last_three_ints_re = re.compile(r'(\s*)(\d+)(\s+)(\d+)(\s+)(\d+)(\s*)$')


def replace_xy_in_line_preserve_format(line: str, new_x: int, new_y: int) -> str:
    m = _last_three_ints_re.search(line)
    if not m:
        return line

    before = line[:m.start(1)]
    sp1, x_old, sp2, y_old, sp3, last, endsp = m.groups()

    x_new_str = str(new_x).rjust(len(x_old))
    y_new_str = str(new_y).rjust(len(y_old))

    return f"{before}{sp1}{x_new_str}{sp2}{y_new_str}{sp3}{last}{endsp}"


def fix_file(input_file: Path, targetStep: float) -> Path:
    raw_lines = input_file.read_text(encoding="utf-8").splitlines()

    parsed = [parse_line(ln) for ln in raw_lines]
    idx_map = [i for i, p in enumerate(parsed) if p is not None]
    parsed = [p for p in parsed if p is not None]

    if len(parsed) < 2:
        out_file = input_file.with_name(input_file.stem + "_ed.txt")
        out_file.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")
        return out_file

    values = [p[1] for p in parsed]
    xs = [p[2] for p in parsed]
    ys = [p[3] for p in parsed]

    angle = regression_angle(values, xs, ys)

    parsed_mut = parsed[:]

    out_lines = raw_lines[:]

    for i in range(1, len(parsed_mut)):
        prev_line, v1, x1, y1 = parsed_mut[i - 1]
        orig_line, v2, x2, y2 = parsed_mut[i]

        dv = (v2 - v1)
        if dv == 0:
            continue

        dist = distance(x1, y1, x2, y2)
        avg_step = dist / dv
        error = avg_step - targetStep
        current_error = error * dv

        x2_new, y2_new = shift_point(x2, y2, angle, -current_error)

        fixed_line = replace_xy_in_line_preserve_format(orig_line, x2_new, y2_new)

        raw_idx = idx_map[i]
        out_lines[raw_idx] = fixed_line

        parsed_mut[i] = (fixed_line, v2, x2_new, y2_new)

    out_file = input_file.with_name(input_file.stem + "_ed.txt")
    out_file.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    return out_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_coords_batch.py <targetStep>")
        print("Example: python fix_coords_batch.py 37.5")
        sys.exit(1)

    try:
        targetStep = float(sys.argv[1])
    except ValueError:
        print("targetStep must be a number, e.g. 37.5")
        sys.exit(1)

    script_dir = Path(__file__).resolve().parent
    txt_files = [Path(p) for p in glob(str(script_dir / "*.txt"))]

    if not txt_files:
        print("No .txt files found next to the script.")
        sys.exit(0)

    done = 0
    for fp in sorted(txt_files):

        if fp.name.endswith("_ed.txt"):
            continue
        try:
            out = fix_file(fp, targetStep)
            print(f"✔ {fp.name} → {out.name}")
            done += 1
        except Exception as ex:
            print(f"✖ {fp.name}: {ex}")

    print(f"\nProcessed files: {done}")


if __name__ == "__main__":
    main()
