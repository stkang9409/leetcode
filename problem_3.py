def median(A, B):

    m, n = len(A), len(B)

    if m > n:
        A, B, m, n = B, A, n, m

    if n == 0:
        raise ValueError

#half_len은 median의 index가 된다.

    imin, imax, half_len = 0, m, (m + n + 1) / 2

# i와 j는  리스트 A,B 임의의 index가 되며 그 길이의 합이 half_len이 된다.

    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i

# 조건 A[i]>B[j-1} and B[j]>A[i-1]에 부합하도록 i와 j의 값을 변경

        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

#조건 안넣으면 리스트 인덱스 범위 벗어나 오류 남.

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

#두 길이의 합이 홀수일 경우 중앙 값은 딱 나온다.

            if (m + n) % 2 == 1:
                return max_of_left
#짝 수일 경우 max_of_left랑 min_of_right의 합을 2로 나눈 값이 중앙 값이 된다.

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0