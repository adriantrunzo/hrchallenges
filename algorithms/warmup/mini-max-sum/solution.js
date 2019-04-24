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

function miniMaxSum (arr) {
  const sorted = arr.sort()

  return {
    min: sorted.slice(0, 4).reduce((sum, value) => sum + value),
    max: sorted.slice(-4).reduce((sum, value) => sum + value)
  }
}

function main () {
  // Parse the input array (always length 5).
  const values = readLine().split(' ').map(v => Number.parseInt(v, 10))
  const result = miniMaxSum(values)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  // Write results in correct order.
  ws.write(`${result.min} ${result.max}`)
  ws.end()
}
