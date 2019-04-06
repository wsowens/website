var canvas;
var ctx;
var width, height;
var board = [];
var CELL_SIZE = 30;
var cell_probability = 0.2;
var CELL_COLOR = "rgb(79, 101, 127)";
var CLEAR_COLOR = "rgb(17,40,60)";

window.addEventListener('load', function() {
    canvas = document.getElementById("board");
    ctx = canvas.getContext("2d");
    console.log(ctx);
    resizeWindow(undefined);
    board = getNewBoard(width/CELL_SIZE, height/CELL_SIZE);

});

function resizeWindow(event) {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    ctx.filter = "blur(8px)";
    console.log("Done resizing");
    console.log(width, height);
    board = getNewBoard(width/CELL_SIZE, height/CELL_SIZE);
}

window.addEventListener('resize', resizeWindow);

function getNewBoard(h, w) {
    console.log("Creating new board");
    let local_board = []
    for (var i = 0; i < h; i++) {
        var row = []
        for (var j = 0; j < w; j++) {
            if (Math.random() <= cell_probability) {
                row.push(true);
            } else {
                row.push(false);
            }
        }
        local_board.push(row);
    }
    console.log(local_board);
    return local_board;
}


function neighborCount(brd, r, c) {
    let count = 0
    if (brd[r][c]) {
        count = -1;
    }
    for (var i = r-1; i <= r+1; i++)
    {
        for (var j = c-1; j <= c+1; j++)
        {
            let cell_i = i;
            let cell_j = j;
            if (cell_i < 0) {
                cell_i = brd.length - 1;
            }
            else if (cell_i > brd.length - 1) {
                cell_i = 0;
            }
            if (cell_j < 0) {
                cell_j = brd[cell_i].length - 1;
            }
            else if (cell_j > brd[cell_i].length - 1) {
                cell_j = 0;
            }
            if (brd[cell_i][cell_j]) {
                count++;
            }
        }
    }
    return count;
}

function generate_counts(brd) {
    let count_brd = []
    for (var i = 0; i < brd.length; i++) {
        var row = []
        for (var j = 0; j < brd[i].length; j++) {
            row.push(neighborCount(brd, i, j));
        }
        count_brd.push(row);
    }
    return count_brd;
}

function advanceBoard(brd) {
    let count_brd = generate_counts(brd);
    for (var i = 0; i < brd.length; i++) {
        for (var j =0; j < brd[i].length; j++) {
            let count = count_brd[i][j];
            //console.log(count, i, j);
            if (brd[i][j]) {
                if ( (count != 2) && (count !=3)) {
                      brd[i][j] = false;
                }
            } else {
                if (count == 3) {
                    brd[i][j] = true;
                }
            }
        }
    } 
}

function renderBoard() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = CELL_COLOR;
    for (var i = 0; i < board.length; i++) {
        for (var j =0; j < board[i].length; j++) {
            if (board[i][j]) {
                ctx.fillRect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE);
            }
        }
    }
}

var last = null
function renderBoard(last):
    if (!start) start = timestamp;
    var delta = timestamp - start;
    if (progress < 2000) {
        advanceBoard(brd);
        renderBoard();
        window.requestAnimationFrame(step);
    }