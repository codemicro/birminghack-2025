def add_coord(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (
        a[0] + b[0],
        a[1] + b[1],
    )


def center_within(canvas_size: tuple[int, int], thing_size: tuple[int, int]) -> tuple[int, int]:
    return (
        int((canvas_size[0] - thing_size[0]) / 2),
        int((canvas_size[1] - thing_size[1]) / 2),
    )
