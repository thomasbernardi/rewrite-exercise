methods {
    foo(uint8[]) envfree;
    summarizeMe(uint256[]) returns uint256 envfree => CONSTANT;
    summarizeMe2(uint256) returns (uint256) => CONSTANT;
    add(uint32,uint32) returns (uint32) envfree;
    doesntExist(bool) returns bool;
}

rule methodInContract {
    if (doesntExist(bool).selector in currentContract) {
        assert false;
    }
    assert true;
}

rule callFoo {
    env e;
    calldataarg args;
    sinvoke foo(e, args);
    assert true;
}

rule doSomeMath(uint32 x, uint32 y) {
    uint32 z = x + y;
    assert z == sinvoke add(x, y);
}