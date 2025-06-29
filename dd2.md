Of course. Here is the C++ solution for the "Tree climber" problem, structured to fit the function signature you provided.

```cpp
#include <vector>
#include <map>
#include <cmath>
#include <functional>

int get_square_free_part(int n) {
    int res = 1;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            int count = 0;
            while (n % i == 0) {
                count++;
                n /= i;
            }
            if (count % 2 == 1) {
                res *= i;
            }
        }
    }
    if (n > 1) {
        res *= n;
    }
    return res;
}

long long solve(int n, std::vector<int>& val, std::vector<std::vector<int>>& edge) {
    if (n <= 1) {
        return 0;
    }

    std::vector<std::vector<int>> adj(n);
    for (const auto& e : edge) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }

    std::vector<int> sf_vals(n);
    for (int i = 0; i < n; ++i) {
        sf_vals[i] = get_square_free_part(val[i]);
    }

    long long total_sum = 0;
    std::map<int, int> path_counts;

    std::function<void(int, int)> dfs = 
        [&](int u, int p) {
        
        int current_sf_val = sf_vals[u];
        
        if (path_counts.count(current_sf_val)) {
            total_sum += path_counts.at(current_sf_val);
        }
        
        path_counts[current_sf_val]++;
        
        for (int v : adj[u]) {
            if (v != p) {
                dfs(v, u);
            }
        }
        
        path_counts[current_sf_val]--;
    };

    dfs(0, -1);

    return total_sum;
}
```