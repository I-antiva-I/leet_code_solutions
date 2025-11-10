// LeetCode #2627 | Debounce | [MEDIUM] |

// (?) https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) 
{   
    let timeoutRef = null;
    
    return function(...args) 
    {
        if (timeoutRef !== null) {clearTimeout(timeoutRef)}
        timeoutRef = setTimeout(fn, t, ...args);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */