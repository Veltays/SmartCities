const fs = require("fs");
const path = require("path");

/**
 * Finds the first parent directory containing a .micropico marker.
 * The search never leaves workspaceRoot.
 */
function findNearestMicroPicoProject(filePath, workspaceRoot) {
    const root = path.resolve(workspaceRoot);
    let current = path.dirname(path.resolve(filePath));

    while (current === root || current.startsWith(root + path.sep)) {
        if (fs.existsSync(path.join(current, ".micropico"))) {
            return current;
        }

        const parent = path.dirname(current);
        if (parent === current) {
            break;
        }
        current = parent;
    }

    return undefined;
}

module.exports = { findNearestMicroPicoProject };
