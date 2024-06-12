/**
 * String: Is Palindrome
 * 
 * Create a function that returns a boolean whether the string is a strict palindrome.
 * Palindrome - string that is same forwards and backwards
 * 
 * Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1= true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!"
const expected4 = false;

function isPalindrome(str){
    for (let i = 0, j = str.length-1; i < j; i++, j--){
        if(str[i] === str[j]){
            return true;
        }
    } 
    return false;
}

console.log(isPalindrome(str1))
console.log(isPalindrome(str2))
console.log(isPalindrome(str3))
console.log(isPalindrome(str4))

// ====================================================================================================

const str1a = "what up, daddy-o?";
const expected1a = "dad";

const str2a = "uh, not much";
const expected2a = "u";

const str3a = "Yikes! my favorite racecar erupted!";
const expected3a = "e racecar e"

const str4a = "a1001x20002y5677765z"
const expected4a = "5677765"

const str5a = "a1001x20002y567765z"
const expected5a = "567765"

// function longestPalindromicSubstring(str){
//     let palindromeIndex = "";
//     for (let i = 0; i < str.length-1; i++){
//         for (let j = str.length-1; j = 0; j--){

//         }
//     }
// }

function longestPalindromicSubstring(str = ""){
    let longestPalindrome = str[0];

    for (let i = 0; i < str.length; i++){
        for (let j = i + 1; j < str.length + 1; j++) {

            let subStr = str.slice(i, j);

            if (subStr.length > longestPalindrome.length && isPalindrome(subStr)) {
                longestPalindrome = subStr
            }
        }
    }
    return longestPalindrome
}

console.log(longestPalindromicSubstring(str1a))
console.log(longestPalindromicSubstring(str2a))
console.log(longestPalindromicSubstring(str3a))
console.log(longestPalindromicSubstring(str4a))
console.log(longestPalindromicSubstring(str5a))