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

// Return the number of integers between the sets.
function getTotalX (a, b) {
  let count = 0
  let num = Math.max(...a)
  let limit = Math.min(...b)

  while (num <= limit) {
    if (
      a.every(x => num % x === 0) &&
      b.every(x => x % num === 0)
    ) {
      count += 1
    }

    num += 1
  }

  return count
}

function main () {
  // We don't need to care about the number of elements in each array.
  readLine()

  const a = readIntegerArray()
  const b = readIntegerArray()
  const result = getTotalX(a, b)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
