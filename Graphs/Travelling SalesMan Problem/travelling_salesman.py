def tsp_dp(dist):
    n = len(dist)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting from city 0 with only city 0 visited

    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j) and i != j:
                        new_cost = dp[mask ^ (1 << i)][j] + dist[j][i]
                        if new_cost < dp[mask][i]:
                            dp[mask][i] = new_cost
                            parent[mask][i] = j

    # The result is the minimum cost to visit all cities and return to the start city
    result = float('inf')
    final_mask = (1 << n) - 1
    last_city = -1
    for i in range(1, n):
        new_cost = dp[final_mask][i] + dist[i][0]
        if new_cost < result:
            result = new_cost
            last_city = i

    # Reconstruct the path
    path = []
    mask = final_mask
    while last_city != -1:
        path.append(last_city)
        next_city = parent[mask][last_city]
        mask ^= (1 << last_city)
        last_city = next_city
    path.append(0)  # Add the starting city

    path.reverse()
    return result, path

# Example distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, path = tsp_dp(dist)
print("The minimum cost is:", min_cost)
print("The path taken is:", path)
