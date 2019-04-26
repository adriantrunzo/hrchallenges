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

// Return the number of ways the chocolate bar can be broken.
// s: squares of the chocolate bar
// d: birthday day, sum of contiguous elements
// m: birthday month, number of contiguous elements
function birthday (s, d, m) {
  let count = 0

  for (let i = 0; (i + (m - 1)) < s.length; i++) {
    const segment = s.slice(i, i + m)
    const sum = segment.reduce((sum, value) => sum + value)

    if (sum === d) {
      count += 1
    }
  }

  return count
}

function main () {
  // We don't need to care about the number of elements in the array.
  readLine()

  const s = readIntegerArray()
  const [d, m] = readIntegerArray()
  const result = birthday(s, d, m)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
