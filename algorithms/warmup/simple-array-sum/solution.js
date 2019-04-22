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

// Return the sum of the array.
function simpleArraySum (arr) {
  return arr.reduce((sum, value) => sum + value)
}

function main () {
  readLine() // We don't need to care about the size of the array.

  // Parse the input array and save the sum.
  const values = readLine().split(' ').map(v => Number.parseInt(v, 10))
  const result = simpleArraySum(values)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
