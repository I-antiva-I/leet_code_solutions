// LeetCode #2723 | Add Two Promises | [EASY] |
// [!] IMPORTANT (Promises)

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) 
{
    // Approach # 1
    /*
    return Promise.all([promise1, promise2]).then((values) => 
    {
        return values.reduce((a,b) => {return a+b}, 0);
    });
    */

    // Approach # 2
    /*
    const v1 = await promise1;
    const v2 = await promise2;
    return v1 + v2;
    */

    // Approach # 3
    const [v1, v2] = await Promise.all([promise1, promise2]);
    return v1 + v2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */