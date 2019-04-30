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

// Return a single integer that denotes the number of valleys Gary walked
// through during his hike.
function countingValleys (steps) {
  let count = 0
  let altitude = 0

  for (const char of steps) {
    if (char === 'U') {
      altitude += 1

      // Hiking back up to sea level denotes a valley.
      if (altitude === 0) {
        count += 1
      }
    } else {
      altitude -= 1
    }
  }

  return count
}

function main () {
  // We don't need to care about the number of steps.
  readLine()

  const steps = readLine()
  const result = countingValleys(steps)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
