methods {
    function foo(Test.Yolo[]) external returns Test.Yeet[] envfree;
    function currentContract.summarizeMe(uint256[]) external returns uint256 envfree;
    function summarizeMe2(uint256) internal returns (uint256) => CONSTANT;
    function add(uint32,uint32) external returns (uint32) envfree;
    function doesntExist(bool) external returns bool optional;
}

my_summary(uint256[] x) {
    return 5;
}

rule methodInContract {
    if (sig:doesntExist(bool).selector in currentContract) {
        assert false;
    }
    assert true;
}

rule callFoo {
    env e;
    calldataarg args;
    foo(e, args);
    assert true;
}

rule doSomeMath(uint32 x, uint32 y) {
    uint32 z = require_uint32(x + y);
    assert z == add(x, y);
}