class textDAO:
    def __init__(self,x):
        self.__x = x
        #
        # VARIABLES FOR THE VARIABLE GOD.
        #
    def get_encounters(self, x, y):
        # y = 4
        subDict = {"NP": " You are alone.{Walk}|wlk"}
        ratDict = {
            "x": "The rats have been slain.|wlk",
            0: " You see the body of a dead rat.|wlk",
            1: " You see a single rat.|cmb",
            2: " You see two rats.|cmb",
            3: " You see a trio of rats.|cmb",
            4: " You see a swarm of rats.|cmb"
        }
        banditDic = {
            "x": " The bandit was defeated.|wlk",
            0: " You see the body of a dead bandit.|mel",
            1: " You see a bandit on the ground at the mercy of your blade.|mel",
            2: " You see an injured bandit.|mel",
            3: " You see a Bandit with eyes full of greed.|mel",
            4: " You see a Bandit with eyes full of greed.|mel"
        }
        monsterDic = {
            "x": "You have slain the monster.|wlk",
            0: " You see no monster.|wlk",
            1: " You see a single monsters.|cmb",
            2: " You see two monsters.|cmb",
            3: " You see a trio of monsters.|cmb",
            4: " You see a swarm of monsters.|cmb"
        }
        trapDict = {
            "x": "You have bested the trap.|wlk",
            0: " a defeated trap.|itr",
            1: " a defeated trap..|itr",
            2: " a sprung trap|itr",
            3: " a disarmed trap.|itr",
            4: " a trap about to spring.|itr"
        }
        puzzleDict= {
            "x": "You have solved the puzzle|wlk",
            0: " You see a solved puzzle|wlk",
            1: " You see a nearly solved puzzle|PZL",
            2: " You see a puzzle.|PZL",
            3: " You see a puzzle.|PZL",
            4: " You see a puzzle.|PZL"
        }
        # encDict= {
        #     "P": puzzleDict[y]
        #     , "R": ratDict[y]
        #     , "M": monsterDic[y]
        #     , "L": " You come across a treasure chest.|itr"
        #     , "0": " The way is cleared. You see a chest.|itr"
        #     , "T": trapDict[y]
        #     , "B": banditDic[y]
        #     , "N": " An angry bandit brandishing a weapon.|cmb"
        #     , "Z": " The Basilisk of Carrows Way appears before you.|tlk"
        #     , "E": " You are alone.{Walk}|wlk"
        # }

        if x == "P":
            output = puzzleDict[y]
        elif x == "R":
            output= ratDict[y]
        elif x == "M":
            output = monsterDic[y]
        elif x == "L":
            output = " a treasure chest.|itr"
        elif x == "0":
            output = " You see a chest.|itr"
        elif x == "T":
            output = trapDict[y]
        elif x == "B":
            output = banditDic[y]
        elif x == "N":
            output = " An angry bandit brandishing a weapon.|cmb"
        elif x == "Z":
            output = " The Basilisk of Carrows Way appears before you.|tlk"
        elif x == "E":
            output = " You are alone.{Walk}|wlk"
        elif x == "H":
            return "For the moment there is respite. Do you brave the depths of Carrows Way again?| {Yes} or {No}."


        return output

    def get_puzzle(self, x):
        #
        # a | 
        #
        puzzleDict = {
            "x":" Choose the {Top}, {Bottom} or {Middle} disk | Then choose to rotate {Right} or {Left}"
        }
        return puzzleDict[x]

    def get_special(self, x, y):
        banditDict = {
            "xx": "|",
            "PSF": " | {Attack} | {Free Shot} | {Item} | {Talk}",
            "ESF": " | {Attack} | {Item}",
            "BP": " | {Attack} | {Item}"
        }
        ratDict = {
            "xx": "|",
            "PSF": " | {Attack} | {Free Shot} | {Item}",
            "ESF": " | {Attack} | {Item}",
            "BP": " | {Attack} | {Item}"
        }
        monsterDict = {
            "xx": "|",
            "PSF": " | {Attack} | {Free Shot} | {Items}",
            "ESF": " | {Attack} | {Item}",
            "BP": " | {Attack} | {Item}"
        }
        trapDict = {
            "xx":"| {Item} | {Disarm}"
        }
        hallDict = {
            "xx": "| {Item} | {Look}"
        }
        if x == "T":
            return trapDict[y]
        elif x == "R":
            return ratDict[y]
        elif x == "B":
            return banditDict[y]
        elif x == "M":
            return monsterDict[y]
        elif x == "E":
            return hallDict[y]
        else:
            return "OPTION ERROR"
        # specialDict= {
        #     "T": trapDict[y],
        #     "R": ratDict[y],
        #     "B": banditDict[y],
        #     "M": monsterDict[y]
        #
        # }

    def get_damage(self, x, job):
        dmgDictBandit = {
            "free Shot": "You strike the unaware opponent and deal $$ damage.|1"
            , "item": "You throw a vile of alchemist fire and deal $$ damage.|1"
            , "attack": "You deal $$ damage as you clash with your opponent.|1"
        }
        dmgDict = {
            "bandit":dmgDictBandit[x]
        }
        return dmgDict[job]

    def get_Dungeon(self, x):
        #
        # B = bandits, mel
        # R = rats, cmb
        # M = monsters, cmb
        # L
        # T
        # P = puzzle, PZL
        #
        # BEREMELETE
        #
        dunDict = { # Direction discription order: North, South, East, West
            "p":"x,1^1,x,x,H,The blessing of the sun warms your core."
            ,
            "1^1": "p,2^1,x,x,BEREMELETE,You stand in a dusty chamber. The sun kissed entrance is to the {north}. "
                   "To the {south} is carved stone passage."
            ,
            "2^1": "1^1,x,2^2,x,BEREMELETE,You stand in dimly lit corridor. Faint light can be seen from the{North} and the passage winds {South}. "
            ,
            "2^2": "x,3^2,x,2^1,BEREMELETE,Pale light shows words of a lost language etched in stone. To the {south} the light fads further. Soft wind trickles from the {east}."
            ,
            "3^2": "2^2,4^2,x,x,BEREMELETE,There are stone carvings on the wall but they have faded with time."
                     "out. The passage continues {north} and {south}."
            ,
            "4^2": "3^2,x,4^3,x,BEREMELETE,You rely on your candle for aid against the gloom. "
                     "The passage moves {north} and turns sharply to the {east}."
            ,
            "4^3": "x,5^3,x,4^2,BEREMELETE,The din is oppressive. You see the passage leading {south} "
                     "and turning sharply {west}."
            ,
            "5^3": "4^3,6^3,x,x,BEREMELETE,You feel the darkness at your heels. The passage way stretches {north} & {south}."
            ,
            "6^2": "x,7^2,6^3,x,BEREMELETE,You nearly step into a pit in the floor but manage to pull back in time. The passage winds {south} & continues {east}." # cave, next to path
            ,
            "6^3": "5^3,x,6^4,6^2,BEREMELETE,You stand at a crossroad. The way [north] leads to the entrance. The corridor continues {East}. The way {west} shows an ancient cave." # The split happens here.
            ,
            "6^4": "x,7^4,x,6^3,BEREMELETE,Somewhere you hear ragged breathing but you cannot place where. The echoes bounce {south} & {west}."
            ,
            "7^2": "6^2,8^2,x,x,BEREMELETE,You see scratches in the walls and floor of the cave that look almost like brick. The cave continues {north} & {south}." # cave
            ,
            "7^4": "6^4,8^4,x,x,BEREMELETE,Your footsteps echo down the long. The passage continues {north} & {south}."
            ,
            "8^2": "7^2,x,8^3,x,BEREMELETE,The smell of mildew and refuse is everywhere. The cave continues {north}. Hidden way, you see a carved passage way to the {west}." # cave, next to path.
            ,
            "8^3": "x,x,8^4,8^2,BEREMELETE,Along the path, you see scrap marks along the walls. The passage continues {west} and {east}."
            ,
            "8^4": "7^4,9^4,8^5,8^3,EEEEEBEEEE,You stand in a circular room with passage ways in every direction. In the center stands a pile of stones." # The spot.
            ,
            "8^5": "x,x,x,8^4,BEREMELETE,A cave in blocks your path. The only way is to backtrack {east}."
            ,
            "9^4": "8^4,x,x,x,BEREMELETE,The hall ends suddenly. You see a pile of stones to the {north}."
        } # 16+1 squares
        try:
            return dunDict[x]
        except KeyError:
            return "You narrowly escape a void."

    def get_interact(self, x, y):
        #
        # Interact works not unlike talk.
        #
        treasureDict = {
            "start": "You find a locked chest.| {Open} the lid.| Examine the {lock}.| Examine the {sides}.^itr"
            ,
            "open": "The lock holds steady.| attempt to {force} the lid open.| examine the {lock}.| examine the {sides}.^itr"
            ,
            "lock": "It's a simple lock, you may be able to pick it| attempt to {pick} the lock.| try to {force} the lid.| examine the {sides}.^itr"
            ,
            "sides": "You walk clockwise around the chest. When you reach the back a second time, you see a lever| {Pull} the lever.^itr"
            ,
            "pull": "The lever slides down and finishes with a satisfying click.| Look {inside}.^itr"
            ,
            "pickFAIL": "Your pick breaks, sealing the lock. | attempt to {force} the lid open.| examine the {lock}.| examine the {sides}."
            ,
            "pickSUCCESS": "The pick strikes true and the lock clatters to the floor| look {inside}.^itr"
            ,
            "forceFAIL": "In your attempt to break the lock you smash the contents of the chest. Bits of broken glass and tarnished coins spills out| {Move} on.^wlk"
            ,
            "forceSUCCESS": "With unerring precision you break the lock off while leaving the chest unmolested.| Look {inside}.^itr"
            ,
            "inside": "Inside you discover pristine coins and a sealed jars filled with an unknown substance. Without thought you place them all within your bag.^wlk"
        }

        secretTreasureDict = {
            "start": " You see a chest waiting in the darkness. It is small enough to fit in your hand.| {Open} the lid.| Examine the {sides}.| Examine the {lock}.^itr"
            ,
            "open": " The lid slides open without protest.| look {inside}.^itr"
            ,
            "lock": " You see no lock. The lids awaits to be opened.| {Open} the lid.| Examine the {sides}.^itr"
            ,
            "force": " There is nothing to force, you do not need to struggle to obtain this prize.| {Open} the lid.| Examine the {sides}.^itr"
            ,
            "pick": " There is no lock to pick.| {Open} the lid.| Examine the {sides}.^itr" # Currently inaccessible
            ,
            "sides": " You walk around the sides. It is an ordinary chest.| {Open} the check | {leave} the chest and walk away.^itr"
            ,
            "leave" : " Is it foolish to accept your accomplishments or is it foolish to deny them? | Accept and {open} the lid| {Deny} and walk away.^itr"
            ,
            "deny" : " You walk away.^wlk"
            ,
            "inside": " Inside you find a fragment of parchment, barely legible in this light. You place it in your pocket.^wlk"
        }

        if x == "L":
            return treasureDict[y]
        elif x == "0":
            return secretTreasureDict[y]
        else:
            return False


    def get_talk(self, x, y):
        talkDict = {
            "00": "This is not a valid option.|tlk"
            , "start": " You meet the Basilisk of Carrows Way. 'Speak adventurer.'"
                     " It hisses from a miasmic cloud. |{OK}|I wish you {peace}|{Hail} and well met|tlk"
            , "ok": "It eyes you dispassionately with a weight of infinite patients."
                  " 'Tell me what you seek.' | A {purpose}.| An {answer}.| enough {Wealth} to live |{Fame}|tlk"
            , "peace": "“How fortuitous.” it chortles mirthlessly. 'These halls lay empty for sometime. What do seek?' | A {purpose}|An {answer}|{Wealth}|{Fame}|tlk"
            , "hail": "its eye reveal a hint of surprise. “Such politeness to a beast such as myself. Do you speak so out of fear or a sense of obligation?”  |{Fear}|{Obligation}|tlk"
            , "fame": "Many live to have their names written in the scrolls of history but few scrolls have survived The End.|{exit}|tlk"
            , "wealth": "Gold and jewels are said to be overrated but few can argue against the comfort they bring. Would you be satisfied with facing The End of luxury?|{exit}|tlk"
            , "answer": "I am sorry to say but you shall not find an answer here.|{exit}|tlk"
            , "fear": "I will not eat my first visitor in eons. Tell me what you wish. |A {purpose}|An {answer}|{Wealth}|{Fame}|tlk"
            , "obligation": "Good to see the old ways are not dead. Tell me what you wish. |A {purpose}|An {answer}|{Wealth}|{Fame}|tlk"
            , "purpose": "In this I cannot help.|{exit}|tlk"
            , "exit": "Luck upon your travels.|wlk"
        }
        if x == "Z":
            return talkDict[y]
        else:
            return False

    def get_traps(self, x, y):
        trapDict = {
            1: " A blade appears from the ceiling and heads straight for you. Jump {Right} or {Left} to avoid|swingR"
            , 2: " From the ceiling a blade appears and heads straight for you. Jump {Right} or {Left} to avoid|swingL"
        }
        return trapDict[x]


    def get_melee(self, x):
        movesDict = {
            "slash": "feint|parry"
            , "lunge": "slash|feint"
            , "push": "lunge|slash"
            , "pierce": "push|lunge"
            , "riposte": "pierce|push"
            , "parry": "riposte|pierce"
            , "feint": "parry|riposte"
        }
        try:
            return movesDict[x]
        except KeyError:
            return "Your strike connects with nothing."

    #Win: feint,