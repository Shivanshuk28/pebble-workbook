#include <cassert>
#include "solution.cpp"

/*
REMEMBER:
- Your tests should be comprehensive. They should test
  - edge cases
  - large inputs
  - as many scenarios as possible.
- Minimum 5 tests. Maximum 10 tests.
- More tests, higher-quality tests === higher payouts.
*/

int main()
{
    assert({entrypoint}(/* args */) == /* expected result */);

    assert({entrypoint}(/* args */) == /* expected result */);

    assert({entrypoint}(/* edge case args */) == /* expected result */);

    assert({entrypoint}(/* large input */) == /* expected result */);

    try
    {
        {entrypoint}(/* invalid args */);
        assert(false);
    }
    catch (const std::invalid_argument &e)
    {
        assert(std::string(e.what()) == "Expected error message");
    }

    assert({entrypoint}(/* args */) == /* expected result */);

    return 0;
}