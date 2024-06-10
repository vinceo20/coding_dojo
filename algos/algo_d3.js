/**
    String Encode

    You are given a string that may contain sequences of consecutive charaters.
    Create a function to shorten a string by including the character.
    then the number of times it appears.


    If final result is not shorter (such as "bb" => "b2"),
    return the original string.
 */

const str1 = "aaaabbcddd";
const exp1 = "a4b2c1d3"

const str2 = ""
const exp2 = ""

const str3 = "a"
const exp3 = "a"

const str4 = "bbcc"
const exp4 = "bbcc"

const str5 = "aaaabbcdddaaaa"
const exp5 = "a8b2c1d3"

function encodeStr(str){
    if (str.length === 0){
        return ""
    }

    let result = ""
    let count = 1

    for (let i = 1; i < str.length; i++){
        if (str[i] === str[i-1]){
            count++
        } else {
            result += str[i-1] + (count > 1 ? count : "")
            count = 1
        }
    }

    result += str[str.length-1] + (count > 1 ? count : "")

    return result
}

function encodeStr1 (str){
    let encoded = "";
    let compareChar = str[0];
    let compareCharCount = 0;

    for (let i = 0; i < str.length; i++){
        const isDuplicated = str[i] === compareChar;
        const isLastIteration = i === str.length - 1;

        if (isDuplicated) {
            compareCharCount++;
        }

        if (isDuplicated === false || isLastIteration){
            encoded += compareChar + compareCharCount;
            compareChar = str[i]
            compareCharCount = 1;
        }
    }
    return encoded.length > 0 && encoded.length < str.length ? encoded : str;
}

console.log(encodeStr1(str5))


// ============================================================================================================================================
/**
 * String Decode
 * 
 */

const string1 = "a3b2c1d3"
const expected1 = "aaabbcddd"

const string2 = "a3b2c12d10"
const expected2 = "aaabbccccccccccccdddddddddd"

function decodeStr(str){
    let decoded = "";
    let i = 0;

    while (i < str.length) {
        let char = str[i++];
        let numStr = "";
        let isNumber = isNaN(parseInt(str[i])) === false;

        while ( i < str.length && isNumber){
            numStr += str[i++];
            isNumber = isNaN(parseInt(str[i])) === false;
        }
        decoded += char.repeat(numStr);
    }
    return decoded;
}

console.log(decodeStr(string1), "-", expected1)