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

function readIntegerArray () {
  return readLine().split(' ').map(v => Number.parseInt(v, 10))
}

// Determines whether the two kangaroos can land at the same location
// after the same number of jumps.
function kangaroo (x1, v1, x2, v2) {
  const n = ((x2 - x1) / (v1 - v2))

  return Number.isInteger(n) && n >= 0
}

function main () {
  const [x1, v1, x2, v2] = readIntegerArray()
  const result = kangaroo(x1, v1, x2, v2)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result ? 'YES' : 'NO'}\n`)
  ws.end()
}
