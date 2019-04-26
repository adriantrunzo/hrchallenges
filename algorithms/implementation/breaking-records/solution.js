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

// Return the number of times the highest and lowest score records were
// broken.
function breakingRecords (scores) {
  let lowest = Infinity
  let highest = -Infinity
  const result = {
    lowest: -1,
    highest: -1
  }

  for (const score of scores) {
    if (score < lowest) {
      lowest = score
      result.lowest += 1
    }

    if (score > highest) {
      highest = score
      result.highest += 1
    }
  }

  return result
}

function main () {
  // We don't need to care about the number of elements in the array.
  readLine()

  const scores = readIntegerArray()
  const result = breakingRecords(scores)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result.highest} ${result.lowest}\n`)
  ws.end()
}
