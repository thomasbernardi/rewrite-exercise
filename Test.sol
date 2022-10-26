contract Test {
    constructor() {

    }

    enum Yolo {
        a,
        b,
        c
    }

    struct Yeet {
        uint256 x;
        Yolo y;
    }

    function foo(Yolo[] calldata x) public pure returns (Yeet[] memory) {
        Yeet[] memory ret = new Yeet[](x.length);
        for (uint i = 0; i < x.length; i++) {
            ret[i] = Yeet(i, x[i]);
        }
        return ret;
    }

    function summarizeMe(uint256[] calldata x) external pure returns (uint256) {
        uint256 ret = 0;
        for (uint i = 0; i < x.length; i++) {
            ret += x[i];
        }
        return ret;
    }

    function summarizeMe2(uint256 x) internal pure returns (uint256) {
        return x**x;
    }

    function add(uint32 x, uint32 y) public pure returns (uint32) {
        return x + y;
    }
}