# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:21:15 2018

@author: NAO
"""

import random as rand

def random_deck(card_rank, draw_count):
    
    Rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
            'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        
    Suit = ['Diamond', 'Heart', 'Club', 'Spade']
        
    deck = []
    sel_card = []
    hits = []
    
    for r in Rank:
        for s in Suit:
            deck.append([r, s])
            
    for i in range(draw_count):
        sel_card.append(rand.choice(deck))
        
    for n in range(len(sel_card)):
        if(sel_card[n][0] == card_rank):
            hits.append(sel_card[n])
            
    print(len(hits), card_rank, "drawn out of", draw_count, "trials.")
    print("Percentage:", round(len(hits) / draw_count, 4),
          "( probability of getting a", card_rank, "is", round(4/52, 4), ")")

            
card_rank = 'Queen'
draw_count = 52            
random_deck(card_rank, draw_count)

draw_count = 52 * 10         
random_deck(card_rank, draw_count)

draw_count = 52 * 100            
random_deck(card_rank, draw_count)