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

// Return the type number of the most common bird; if two or more types
// of birds are equally common, choose the type with the smallest ID number.
function migratoryBirds (arr) {
  const counts = {}
  const sorted = arr.sort()
  let maxId = sorted[0]

  for (const id of sorted) {
    counts[id] = counts[id] ? counts[id] + 1 : 1

    if (counts[id] > counts[maxId]) {
      maxId = id
    }
  }

  return maxId
}

function main () {
  // We don't need to care about the length of the incoming array.
  readLine()

  const sightings = readIntegerArray()
  const result = migratoryBirds(sightings)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
