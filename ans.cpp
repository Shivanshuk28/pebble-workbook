#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <queue>
#include <bits/stc++.h>


using namespace std;

// Precompute smallest prime factors for efficient factorization
vector<int> precompute_spf(int max_val) {
    vector<int> spf(max_val + 1);
    for (int i = 2; i <= max_val; i++) {
        if (spf[i] == 0) {
            spf[i] = i;
            for (long long j = (long long)i * i; j <= max_val; j += i) {
                if (spf[j] == 0) spf[j] = i;
            }
        }
    }
    return spf;
}

// Get square-free part (product of primes with odd exponents)
int get_square_free(int x, const vector<int>& spf) {
    if (x == 1) return 1;
    int res = 1;
    while (x > 1) {
        int p = spf[x];
        int cnt = 0;
        while (x % p == 0) {
            x /= p;
            cnt++;
        }
        if (cnt % 2 == 1) res *= p;
    }
    return res;
}

long long solve(int n, vector<int>& val, vector<vector<int>>& edges) {
    const int max_val = *max_element(val.begin(), val.end());
    auto spf = precompute_spf(max_val);
    
    // Build adjacency list and tree structure
    vector<vector<int>> adj(n);
    for (const auto& edge : edges) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
    }
    
    vector<int> parent(n, -1);
    vector<vector<int>> children(n);
    queue<int> q;
    q.push(0);
    parent[0] = -2;
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (parent[v] == -1) {
                parent[v] = u;
                children[u].push_back(v);
                q.push(v);
            }
        }
    }
    
    long long total = 0;
    unordered_map<int, int> freq;
    
    // DFS with path tracking
    vector<pair<int, bool>> stack;
    stack.emplace_back(0, false);
    
    while (!stack.empty()) {
        auto [node, processed] = stack.back();
        stack.pop_back();
        
        if (processed) {
            // Remove current node from frequency map
            int sf = get_square_free(val[node], spf);
            freq[sf]--;
            continue;
        }
        
        if (node != 0) {
            // Calculate v_i for current node
            int sf = get_square_free(val[node], spf);
            total += freq[sf];
        }
        
        // Mark as processed and push back
        stack.emplace_back(node, true);
        
        // Add current node to frequency map
        int sf = get_square_free(val[node], spf);
        freq[sf]++;
        
        // Push children in reverse order
        for (auto it = children[node].rbegin(); it != children[node].rend(); ++it) {
            stack.emplace_back(*it, false);
        }
    }
    
    return total;
}

int main() {
    // Example usage
    int n = 3;
    vector<int> val = {2, 8, 18};
    vector<vector<int>> edges = {{0, 1}, {1, 2}};
    
    cout << solve(n, val, edges) << endl;  // Output: 3
    
    return 0;
}



// #include <iostream>
// #include <vector>
// #include <cmath>
// #include <queue>
// #include <unordered_map>

// using namespace std;

// long long solve(int n, vector<int>& val, vector<vector<int>>& edges) {
//     // Build adjacency list
//     vector<vector<int>> adj(n);
//     for (const auto& edge : edges) {
//         int u = edge[0];
//         int v = edge[1];
//         adj[u].push_back(v);
//         adj[v].push_back(u);
//     }

//     // BFS to establish parent-child relationships
//     vector<int> parent(n, -1);
//     vector<vector<int>> children(n);
//     queue<int> q;
//     q.push(0);
//     parent[0] = -2;  // Mark root's parent differently

//     while (!q.empty()) {
//         int u = q.front();
//         q.pop();
//         for (int v : adj[u]) {
//             if (parent[v] == -1) {
//                 parent[v] = u;
//                 children[u].push_back(v);
//                 q.push(v);
//             }
//         }
//     }

//     long long total = 0;

//     // DFS stack elements: (node, path from root)
//     vector<pair<int, vector<int>>> stack;
//     stack.emplace_back(0, vector<int>());

//     while (!stack.empty()) {
//         auto [node, path] = stack.back();
//         stack.pop_back();

//         if (node != 0) {
//             // Compute v_i for current node
//             int v_i = 0;
//             for (int j : path) {
//                 long long product = (long long)val[node] * val[j];
//                 long long root = sqrt(product);
//                 if (root * root == product) {
//                     v_i++;
//                 }
//             }
//             total += v_i;
//         }

//         // Prepare new path for children
//         vector<int> new_path = path;
//         new_path.push_back(node);

//         // Push children in reverse order to process them in order
//         for (auto it = children[node].rbegin(); it != children[node].rend(); ++it) {
//             stack.emplace_back(*it, new_path);
//         }
//     }

//     return total;
// }

// int main() {
//     // Example usage:
//     int n = 3;
//     vector<int> val = {2, 8, 18};
//     vector<vector<int>> edges = {{0, 1}, {1, 2}};
    
//     cout << solve(n, val, edges) << endl;  // Output: 3
    
//     return 0;
// }