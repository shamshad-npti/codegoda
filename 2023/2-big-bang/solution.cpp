#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef long long ll;

class Body {
    public:
        ll mass;
        ll momentum;

        Body(ll mass, ll momentum) {
            this->mass = mass;
            this->momentum = momentum;
        }

        bool operator < (const Body& other) const {
            // check this->momentum * other->mass < this->mass * other->momentum will result in integer overflow (64 bits)
            // so we use long division to compare the two fraction
            // Challenge: what is the minimum number of iterations sufficient to compare the two fractions given the input constraints?

            ll momentum1 = this->momentum, momentum2 = other.momentum;
            for(int i = 0; i < 15; i++) {
                ll v1 = momentum1 / this->mass, v2 = momentum2 / other.mass;
                if(v1 != v2)
                    return v1 < v2;
                momentum1 = (momentum1 % this->mass)*10;
                momentum2 = (momentum2 % other.mass)*10;
            }
            return false;
        }

        Body operator + (const Body& other) const {
            return Body(this->mass + other.mass, this->momentum + other.momentum);
        }
};

int main() {
    int n;
    cin >> n;
    vector<ll> masses(n), velocities(n);
    for(int i = 0; i < n; i++)
        cin >> masses[i];
    for(int i = 0; i < n; i++)
        cin >> velocities[i];
    vector<Body> bodies;
    for(int i = 0; i < n; i++) {
        Body body(masses[i], masses[i]*velocities[i]);
        while(!bodies.empty() && body < bodies.back()) {
            body = body + bodies.back();
            bodies.pop_back();
        }
        bodies.push_back(body);
    }

    sort(bodies.begin(), bodies.end(), [](const Body& b1, const Body& b2) {
        return b1.mass == b2.mass ? b1.momentum < b2.momentum : b1.mass < b2.mass;
    });

    cout << bodies.size() << endl;
    for(int i = 0; i < bodies.size(); i++)
        cout << bodies[i].mass << " " << bodies[i].momentum << endl;
}