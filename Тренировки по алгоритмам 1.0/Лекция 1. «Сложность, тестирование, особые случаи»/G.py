def parts(alloy_m, wp_m, part_m):
    if alloy_m < wp_m:
        return 0
    if wp_m < part_m:
        return 0
    wp_cnt = alloy_m // wp_m
    part_cnt_from_one_wp = wp_m // part_m
    ext_alloy_m = (alloy_m - wp_m * wp_cnt) + (wp_m - part_cnt_from_one_wp * part_m) * wp_cnt
    return part_cnt_from_one_wp * wp_cnt + parts(ext_alloy_m, wp_m, part_m)

def main():
    alloy_mass, workpiece_mass, part_mass = list(map(int, input().split()))
    print(parts(alloy_mass, workpiece_mass, part_mass))


if __name__ == '__main__':
    main()
