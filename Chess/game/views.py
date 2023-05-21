import json
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Board

# Create your views here.
def figures(board):
    for index,line in enumerate(board):
        if index == 0:
            line[0]['figure'] = 'rook-white'
            line[1]['figure'] = 'knite-white'
            line[2]['figure'] = 'bishop-white'
            line[3]['figure'] = 'king-white'
            line[4]['figure'] = 'queen-white'
            line[5]['figure'] = 'bishop-white'
            line[6]['figure'] = 'knite-white'
            line[7]['figure'] = 'rook-white'
        elif index == 1:
            for i in range(8):
                line[i]['figure'] = 'pone-white'
        elif index == 6:
            for i in range(8):
                line[i]['figure'] = 'pone-black'
        elif index == 7:
            line[0]['figure'] = 'rook-black'
            line[1]['figure'] = 'knite-black'
            line[2]['figure'] = 'bishop-black'
            line[3]['figure'] = 'king-black'
            line[4]['figure'] = 'queen-black'
            line[5]['figure'] = 'bishop-black'
            line[6]['figure'] = 'knite-black'
            line[7]['figure'] = 'rook-black'
    return board

def make_board():
    board = []
    for y in range(1,9):
        line = []
        for x in range(1,9):
            if not y % 2 == 0:
                if x % 2 == 0:
                    cell = {
                        'color':'black',
                        'x':x,
                        'y':y
                    }
                    line.append(cell)
                else:
                    cell = {
                        'color':'white',
                        'x':x,
                        'y':y
                    }
                    line.append(cell)
            else:
                if x % 2 == 0:
                    cell = {
                        'color':'white',
                        'x':x,
                        'y':y
                    }
                    line.append(cell)
                else:
                    cell = {
                        'color':'black',
                        'x':x,
                        'y':y
                    }
                    line.append(cell)
        board.append(line)
        
    return board

DB_PATH = os.path.join(settings.BASE_DIR,'game','static','db.json')

def read_db():
    with open(DB_PATH, 'r') as f:
        return json.loads(f.read())

def write_db(board):
    with open(DB_PATH, 'w') as f:
        return f.write(json.dumps(board))

def collect_board():
    if not os.path.isfile(DB_PATH):
        board = make_board()
        board_with_figure = figures(board)
        write_db(board_with_figure)
    else:
        board_with_figure = read_db()
    # board = Board.objects.create(board=board)
    return board_with_figure

def move_figure(from_x=0,from_y=0,to_x=1,to_y=1):
    board = read_db()
    figure = board[from_y][from_x]["figure"]
    board[from_y][from_x]["figure"] = None
    board[to_y][to_x]["figure"] = figure
    write_db(board)
    return board

def move(request):
    # from_x = int(request.POST.get('from_x'))
    # from_y = int(request.POST.get('from_y'))
    # to_x = int(request.POST.get('to_x'))   
    # to_y = int(request.POST.get('to_y'))
    board = move_figure()
    return JsonResponse(board, safe=False)
    # return redirect('game')


def game(request):
    board = collect_board()
    context = {
        'board':board
    }
    return render(request, 'game/board.html', context)

