n = int(input())
versions = [input().strip() for _ in range(n)]




def parse_version(version):
    if ' ' in version:
        main_part, beta_part = version.split(' ')
        beta_number = (0,int(beta_part[4:]))
    else:
        main_part = version
        beta_number = (1,)

    main_nums = tuple(map(int, main_part.split('.')))

    if len(main_nums) < 4:
        main_nums += (-1,) * (4 - len(main_nums))

    return main_nums + beta_number



sorted_versions = sorted(versions, key=parse_version)



for v in sorted_versions:
    print(v)