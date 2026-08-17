class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        mp ={}
        for i in hand:
            mp[i] = mp.get(i,0)+1

        hand.sort()

        # Step 3: Greedily build groups
        for card in hand:
            count = mp[card]
            
            # If this card has already been used in previous groups, skip
            if count == 0:
                continue
            
            # This card must form a group of size `groupSize`
            for i in range(card, card + groupSize):
                if mp.get(i, 0) < count:
                    return False
                mp[i] -= count
                
        return True


        