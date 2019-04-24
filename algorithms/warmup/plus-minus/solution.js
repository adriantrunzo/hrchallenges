'use strict'

const { createWriteStream } = require('fs')

// Swtich stdin into flowing mode.
process.stdin.resume()
process.stdin.setEncoding('utf-8')

let input = ''
let inputIndex = 0

// Add incoming data to the input buffer.
process.stdin.on('data', chunk => {
  input += chunk
})

// When there is no more input to be read, split it into an array
// and call main().
process.stdin.on('end', () => {
  input = input.trim().split('\n').map(s => s.trim())
  main()
})

// Helper method to read the next input line from the buffer.
function readLine () {
  return input[inputIndex++]
}

function plusMinus (arr) {
  let zero = 0
  let positive = 0
  let negative = 0

  for (const n of arr) {
    if (n > 0) {
      positive += 1
    } else if (n < 0) {
      negative += 1
    } else {
      zero += 1
    }
  }

  return {
    zero: (zero / arr.length),
    positive: (positive / arr.length),
    negative: (negative / arr.length)
  }
}

function main () {
  readLine() // We don't need to care about the size of the array.

  // Parse the input array.
  const values = readLine().split(' ').map(v => Number.parseInt(v, 10))
  const result = plusMinus(values)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  // Write results in correct order and match 6 decimal places.
  ws.write(`${result.positive.toFixed(6)}\n`)
  ws.write(`${result.negative.toFixed(6)}\n`)
  ws.write(`${result.zero.toFixed(6)}\n`)

  ws.end()
}
