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

// Returns a single integer denoting the maximum number of integers you
// can choose from the array such that the absolute difference between any
// two of the chosen integers is <= 1.
function pickingNumbers (numbers) {
  const counts = {}

  for (const number of numbers) {
    counts[number] = counts[number] ? counts[number] + 1 : 1
  }

  const keys = Object.keys(counts).sort()
  let total = counts[keys[0]]

  for (let i = 1; i < keys.length; i++) {
    if (keys[i] - keys[i - 1] === 1) {
      const sum = counts[keys[i]] + counts[keys[i - 1]]

      if (sum > total) {
        total = sum
      }
    } else {
      // Not consecutive.
      if (counts[keys[i]] > total) {
        total = counts[keys[i]]
      }
    }
  }

  return total
}

function main () {
  // We don't need to care about the number of numbers.
  readLine()

  const numbers = readIntegerArray()
  const result = pickingNumbers(numbers)

  // Open the output stream.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
