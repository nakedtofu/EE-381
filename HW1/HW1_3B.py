# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:29:47 2018

@author: NAO
"""

import random as rand
import copy

def random_deck2(card_rank, card_suit, trial_count):
    
    Rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
            'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        
    Suit = ['Diamond', 'Heart', 'Club', 'Spade']
        
    deck = []
    sel_cards = []
    trial = []
    hit = []
    
    for r in Rank:
        for s in Suit:
            deck.append([r, s])
            
    for i in range(trial_count):
        sel_cards.append(rand.choice(deck))
        deck.remove(sel_cards[0])
        sel_cards.append(rand.choice(deck))
        deck.append(sel_cards[0])
        
        trial.append(copy.deepcopy(sel_cards))
        sel_cards.clear()
        
    for n in range(len(trial)):
        if((trial[n][0][0] == card_rank and trial[n][0][1] == card_suit) or 
           #rank suit 1st card
           (trial[n][0][0] == card_rank and trial[n][1][1] == card_suit) or 
           #rank 1st card suit 2nd card
           (trial[n][1][0] == card_rank and trial[n][0][1] == card_suit) or 
           #rank 2nd card suit 1st card
           (trial[n][1][0] == card_rank and trial[n][1][1] == card_suit)):  
            #rank suit 2nd card
            
            hit.append(trial[n])
            
    print("One", card_rank, "one", card_suit, "drawn:",
          len(hit), "( out of", trial_count, "trials )")
    print("Percentage:", round(len(hit) / trial_count, 4),
          "( probability of getting a", card_rank,
          "is", round(15/52*14/51, 4), ")")

            
card_rank = 'Queen'
card_suit = 'Diamond'
trial_count = 52
random_deck2(card_rank, card_suit, trial_count)

trial_count = 52 * 10   
random_deck2(card_rank, card_suit, trial_count)

trial_count = 52 * 100            
random_deck2(card_rank, card_suit, trial_count)
