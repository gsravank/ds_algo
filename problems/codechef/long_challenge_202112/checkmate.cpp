#include <iostream>
#include <utility>
#include <vector>

using namespace std;

bool is_in_check(int xk, int yk, int x1, int y1) {
    if( xk == x1 && yk == y1) {
        return false;
    }
    else {
        if( xk == x1 || yk == y1 ){ 
            return true;
        } else {
            return false;
        }
    }
}

bool move_possible(int xk, int yk, int x1, int y1, int x2, int y2) {
    bool move_found = false;
    for( int x_diff = -1; x_diff < 2; x_diff++) {// in [-1, 0, 1]:
        for( int y_diff=-1; y_diff < 2; y_diff++){// in [-1, 0, 1]:
            if( x_diff != 0 || y_diff != 0){
                int x_new = xk + x_diff;
                int y_new = yk + y_diff;

                if( 1 <= x_new && x_new <= 8 && 1 <= y_new && y_new <= 8) {
                    if( !(is_in_check(x_new, y_new, x1, y1) || is_in_check(x_new, y_new, x2, y2)) ){
                        move_found = true;
                    }
                }
            }
        }
    }

    return move_found;
}


vector<pair<int, int> > get_next_rook_positions(int x, int y, int x_other, int y_other) {
    vector< pair<int, int> > positions;
    if( x == x_other){
        // vertical moves
        int min_height, max_height;
        min_height = y < y_other ? 1 : y_other + 1;
        max_height = y > y_other ? 8 : y_other - 1;
        for (int idx=min_height; idx < max_height + 1; idx++) { // range(min_height, max_height + 1):
            positions.push_back(make_pair(x, idx));
        }
        // horizontal moves
        for(int idx=1; idx < 9; idx++) {// in range(1, 9):
            positions.push_back(make_pair(idx, y));
        }
    } else if( y == y_other) {
        // vertical moves
        for(int idx=1; idx < 9; idx++) {// in range(1, 9):
            positions.push_back(make_pair(x, idx));
        }
        // horizontal moves
        int min_width, max_width;
        min_width = x < x_other ? 1 : x_other + 1;
        max_width = x > x_other ? 8 : x_other - 1;
        for( int idx=min_width; idx < max_width + 1; idx++) { // range(min_width, max_width + 1):
            positions.push_back(make_pair(idx, y));
        }
    } else {
        for(int idx=1; idx < 9; ++idx){ // in range(1, 9):
            positions.push_back(make_pair(idx, y));
        }
        for(int idx=1; idx < 9; ++idx){ // in range(1, 9):
            positions.push_back(make_pair(x, idx));
        }
    }
    return positions;
}


bool can_check_mate(int xk, int yk, int x1, int y1, int x2, int y2){
    // Check next position for each rook
    // Check if the move produces a check && king has no other move
    // print(x1, y1)
    // pair<int, int> pos;
    for (auto pos : get_next_rook_positions(x1, y1, x2, y2)) {
        int x1_new = pos.first;
        int y1_new = pos.second;
        // print(x1_new, y1_new)
        if( x1_new != x2 || y1_new != y2 ) {
            if( (is_in_check(xk, yk, x1_new, y1_new) || is_in_check(xk, yk, x2, y2)) && !move_possible(xk, yk, x1_new, y1_new, x2, y2)) {
                return true;
            }
        }
    }

    // print(x2, y2)
    for( auto pos : get_next_rook_positions(x2, y2, x1, y1)) {
        // print(x2_new, y2_new)
        int x2_new = pos.first;
        int y2_new = pos.second;
        if( x2_new != x2 || y2_new != y2 ) {
            if((is_in_check(xk, yk, x1, y1) || is_in_check(xk, yk, x2_new, y2_new)) && !move_possible(xk, yk, x1, y1, x2_new, y2_new)) {
                return true;
            }
        }
    }

    return false;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);
    int t;
    int x_k, y_k, x_1, x_2, y_1, y_2; 
    cin >> t;
    for (int i = 0; i < t; ++i) {
    cin >> x_k; cin >> y_k;
    cin >> x_1; cin >> y_1;
    cin >> x_2; cin >> y_2;

    if (can_check_mate(x_k, y_k, x_1, y_1, x_2, y_2)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    }
    return 0;
}