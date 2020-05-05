#!/usr/bin/node
exports.callMeMoby = function(num, func) {
    for (let i = 0; i < num; i += 1) {
        func();
    }
}
