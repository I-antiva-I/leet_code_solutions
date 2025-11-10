// LeetCode #2627 | Debounce | [MEDIUM] |

// (?) https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout

type F = (...args: number[]) => void

function debounce(fn: F, t: number): F 
{
    let timerRef: ReturnType<typeof setTimeout> | null = null;
    
    return function(...args) 
    {
        if (timerRef !== null) {clearTimeout(timerRef)}
        timerRef = setTimeout(fn, t, ...args);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */