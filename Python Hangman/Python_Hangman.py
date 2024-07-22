import random


def GameSetUp():

    WordList= ['about', ' above', ' abuse', ' accept', ' accident', ' accuse', ' across', ' activist', ' actor', ' administration', ' admit', ' adult', ' advertise', ' advise', ' affect', ' afraid', ' after', ' again', ' against', ' agency', ' aggression', ' agree', ' agriculture', ' force', ' airplane', ' airport', ' album', ' alcohol', ' alive', ' almost', ' alone', ' along', ' already', ' although', ' always', ' ambassador', ' amend', ' ammunition', ' among', ' amount', ' anarchy', ' ancestor', ' ancient', ' anger', ' animal', ' anniversary', ' announce', ' another', ' answer', ' apologize', ' appeal', ' appear', ' appoint', ' approve', ' archeology', ' argue', ' around', ' arrest', ' arrive', ' artillery', ' assist', ' astronaut', ' astronomy', ' asylum', ' atmosphere', ' attach', ' attack', ' attempt', ' attend', ' attention', ' automobile', ' autumn', ' available', ' average', ' avoid', ' awake', ' award', ' balance', ' balloon', ' ballot', ' barrier', ' battle', ' beauty', ' because', ' become', ' before', ' begin', ' behavior', ' behind', ' believe', ' belong', ' below', ' betray', ' better', ' between', ' biology', ' black', ' blame', ' bleed', ' blind', ' block', ' blood', ' border', ' borrow', ' bottle', ' bottom', ' boycott', ' brain', ' brave', ' bread', ' Break', ' breathe', ' bridge', ' brief', ' bright', ' bring', ' broadcast', ' brother', ' brown', ' budget', ' build', ' building', ' bullet', ' burst', ' business', ' cabinet', ' camera', ' campaign', ' cancel', ' cancer', ' candidate', ' capital', ' capture', ' career', ' careful', ' carry', ' catch', ' cause', ' ceasefire', ' celebrate', ' center', ' century', ' ceremony', ' chairman', ' champion', ' chance', ' change', ' charge', ' chase', ' cheat', ' cheer', ' chemicals', ' chemistry', ' chief', ' child', ' children', ' choose', ' circle', ' citizen', ' civilian', ' civil', ' rights', ' claim', ' clash', ' Class', ' clean', ' clear', ' clergy', ' climate', ' climb', ' clock', ' close', ' cloth', ' clothes', ' cloud', ' coalition', ' coast', ' coffee', ' collapse', ' collect', ' college', ' colony', ' color', ' combine', ' command', ' comment', ' committee', ' common', ' communicate', ' community', ' company', ' compare', ' compete', ' complete', ' Complex', ' compromise', ' computer', ' concern', ' condemn', ' condition', ' conference', ' confirm', ' conflict', ' congratulate', ' Congress', ' connect', ' conservative', ' consider', ' constitution', ' contact', ' contain', ' container', ' continent', ' Continue', ' control', ' convention', ' cooperate', ' correct', ' corruption', ' cotton', ' count', ' country', ' court', ' cover', ' crash', ' create', ' creature', ' credit', ' crime', ' criminal', ' crisis', ' criticize', ' crops', ' cross', ' crowd', ' crush', ' culture', ' curfew', ' current', ' custom', ' customs', ' damage', ' dance', ' danger', ' daughter', ' debate', ' decide', ' declare', ' decrease', ' defeat', ' defend', ' deficit', ' define', ' degree', ' delay', ' delegate', ' demand', ' democracy', ' demonstrate', ' denounce', ' depend', ' deplore', ' deploy', ' depression', ' describe', ' desert', ' design', ' desire', ' destroy', ' detail', ' detain', ' develop', ' device', ' dictator', ' different', ' difficult', ' dinner', ' diplomat', ' direct', ' direction', ' disappear', ' disarm', ' disaster', ' discover', ' discrimination', ' discuss', ' disease', ' dismiss', ' dispute', ' dissident', ' distance', ' divide', ' doctor', ' document', ' dollar', ' donate', ' double', ' dream', ' drink', ' drive', ' drown', ' during', ' early', ' earth', ' earthquake', ' ecology', ' economy', ' education', ' effect', ' effort', ' either', ' elect', ' electricity', ' embassy', ' embryo', ' emergency', ' emotion', ' employ', ' empty', ' enemy', ' energy', ' enforce', ' engine', ' engineer', ' enjoy', ' enough', ' enter', ' environment', ' equal', ' equipment', ' escape', ' especially', ' establish', ' estimate', ' ethnic', ' evaporate', ' event', ' every', ' evidence', ' exact', ' examine', ' example', ' excellent', ' Except', ' exchange', ' excuse', ' execute', ' exercise', ' exile', ' exist', ' expand', ' expect', ' expel', ' experience', ' experiment', ' expert', ' explain', ' explode', ' explore', ' export', ' express', ' extend', ' extra', ' extraordinary', ' extreme', ' extremist', ' factory', ' false', ' family', ' famous', ' father', ' favorite', ' federal', ' female', ' fence', ' fertile', ' field', ' fierce', ' fight', ' final', ' financial', ' finish', ' fireworks', ' first', ' Float', ' flood', ' floor', ' flower', ' fluid', ' follow', ' force', ' foreign', ' forest', ' forget', ' forgive', ' former', ' forward', ' freedom', ' freeze', ' fresh', ' friend', ' frighten', ' front', ' fruit', ' funeral', ' future', ' gather', ' general', ' generation', ' genocide', ' gentle', ' glass', ' goods', ' govern', ' government', ' grain', ' grass', ' great', ' green', ' grind', ' ground', ' group', ' guarantee', ' guard', ' guerrilla', ' guide', ' guilty', ' happen', ' happy', ' harvest', ' headquarters', ' health', ' heavy', ' helicopter', ' hijack', ' history', ' holiday', ' honest', ' honor', ' horrible', ' horse', ' hospital', ' hostage', ' hostile', ' hotel', ' house', ' however', ' human', ' humor', ' hunger', ' hurry', ' husband', ' identify', ' ignore', ' illegal', ' imagine', ' immediate', ' immigrant', ' Import', ' important', ' improve', ' incident', ' incite', ' include', ' increase', ' independent', ' individual', ' industry', ' infect', ' inflation', ' influence', ' inform', ' information', ' inject', ' injure', ' innocent', ' insane', ' insect', ' inspect', ' instead', ' instrument', ' insult', ' intelligence', ' intelligent', ' intense', ' interest', ' interfere', ' international', ' Internet', ' intervene', ' invade', ' invent', ' invest', ' investigate', ' invite', ' involve', ' island', ' issue', ' jewel', ' joint', ' judge', ' justice', ' kidnap', ' knife', ' knowledge', ' labor', ' laboratory', ' language', ' large', ' laugh', ' launch', ' learn', ' leave', ' legal', ' legislature', ' letter', ' level', ' liberal', ' light', ' lightning', ' limit', ' liquid', ' listen', ' literature', ' little', ' local', ' lonely', ' loyal', ' machine', ' magazine', ' major', ' majority', ' manufacture', ' march', ' market', ' marry', ' material', ' mathematics', ' matter', ' mayor', ' measure', ' media', ' medicine', ' member', ' memorial', ' memory', ' mental', ' message', ' metal', ' method', ' microscope', ' middle', ' militant', ' military', ' militia', ' mineral', ' minister', ' minor', ' minority', ' minute', ' missile', ' missing', ' mistake', ' model', ' moderate', ' modern', ' money', ' month', ' moral', ' morning', ' mother', ' motion', ' mountain', ' mourn', ' movement', ' movie', ' murder', ' music', ' mystery', ' narrow', ' nation', ' native', ' natural', ' nature', ' necessary', ' negotiate', ' neighbor', ' neither', ' neutral', ' never', ' night', ' noise', ' nominate', ' normal', ' north', ' nothing', ' nowhere', ' nuclear', ' number', ' Object', ' observe', ' occupy', ' ocean', ' offensive', ' offer', ' office', ' officer', ' official', ' often', ' operate', ' opinion', ' oppose', ' opposite', ' oppress', ' orbit', ' order', ' organize', ' other', ' overthrow', ' paint', ' paper', ' parachute', ' parade', ' pardon', ' parent', ' parliament', ' partner', ' party', ' passenger', ' passport', ' patient', ' peace', ' people', ' percent', ' perfect', ' perform', ' period', ' permanent', ' permit', ' person', ' persuade', ' physical', ' physics', ' picture', ' piece', ' pilot', ' place', ' planet', ' plant', ' plastic', ' please', ' plenty', ' point', ' poison', ' police', ' policy', ' politics', ' pollute', ' popular', ' population', ' position', ' possess', ' possible', ' postpone', ' poverty', ' power', ' praise', ' predict', ' pregnant', ' present', ' president', ' press', ' pressure', ' prevent', ' price', ' prison', ' private', ' prize', ' probably', ' problem', ' process', ' produce', ' profession', ' professor', ' profit', ' program', ' progress', ' project', ' promise', ' propaganda', ' property', ' propose', ' protect', ' protest', ' prove', ' provide', ' public', ' publication', ' publish', ' punish', ' purchase', ' purpose', ' quality', ' question', ' quick', ' quiet', ' radar', ' radiation', ' radio', ' railroad', ' Raise', ' reach', ' react', ' ready', ' realistic', ' reason', ' reasonable', ' rebel', ' receive', ' recent', ' recession', ' recognize', ' record', ' recover', ' reduce', ' reform', ' refugee', ' refuse', ' register', ' regret', ' reject', ' relations', ' release', ' religion', ' remain', ' remains', ' remember', ' remove', ' repair', ' repeat', ' report', ' represent', ' repress', ' request', ' require', ' rescue', ' research', ' resign', ' resist', ' resolution', ' resource', ' respect', ' responsible', ' restaurant', ' restrain', ' restrict', ' result', ' retire]', ' return', ' revolt', ' right', ' river', ' rocket', ' rough', ' Round', ' rubber', ' rural', ' sabotage', ' sacrifice', ' sailor', ' satellite', ' satisfy', ' school', ' science', ' search', ' season', ' second', ' secret', ' security', ' seeking', ' seize', ' Senate', ' sense', ' sentence', ' separate', ' series', ' serious', ' serve', ' service', ' settle', ' several', ' severe', ' shake', ' shape', ' share', ' sharp', ' sheep', ' shell', ' shelter', ' shine', ' shock', ' shoot', ' short', ' should', ' shout', ' shrink', ' sickness', ' signal', ' silence', ' silver', ' similar', ' simple', ' since', ' single', ' sister', ' situation', ' skeleton', ' skill', ' slave', ' sleep', ' slide', ' small', ' smash', ' smell', ' smoke', ' smooth', ' social', ' soldier', ' solid', ' solve', ' sound', ' south', ' space', ' speak', ' special', ' speech', ' speed', ' spend', ' spill', ' spirit', ' split', ' sport', ' spread', ' spring', ' square', ' stand', ' start', ' starve', ' state', ' station', ' statue', ' steal', ' steam', ' steel', ' stick', ' still', ' stone', ' store', ' storm', ' story', ' stove', ' straight', ' strange', ' street', ' stretch', ' strike', ' strong', ' structure', ' struggle', ' study', ' stupid', ' subject', ' submarine', ' substance', ' substitute', ' subversion', ' succeed', ' sudden', ' suffer', ' sugar', ' suggest', ' suicide', ' summer', ' supervise', ' supply', ' support', ' suppose', ' suppress', ' surface', ' surplus', ' surprise', ' surrender', ' surround', ' survive', ' suspect', ' suspend', ' swallow', ' swear', ' sweet', ' sympathy', ' system', ' target', ' taste', ' teach', ' technical', ' technology', ' telephone', ' telescope', ' television', ' temperature', ' temporary', ' tense', ' terrible', ' territory', ' terror', ' terrorist', ' thank', ' theater', ' theory', ' there', ' these', ' thick', ' thing', ' think', ' third', ' threaten', ' through', ' throw', ' tired', ' today', ' together', ' tomorrow', ' tonight', ' torture', ' total', ' touch', ' toward', ' trade', ' tradition', ' traffic', ' tragic', ' train', ' transport', ' transportation', ' travel', ' treason', ' treasure', ' treat', ' treatment', ' treaty', ' trial', ' tribe', ' trick', ' troops', ' trouble', ' truce', ' truck', ' trust', ' under', ' understand', ' unite', ' universe', ' university', ' unless', ' until', ' urgent', ' usual', ' vacation', ' vaccine', ' valley', ' value', ' vegetable', ' vehicle', ' version', ' victim', ' victory', ' video', ' village', ' violate', ' violence', ' visit', ' voice', ' volcano', ' volunteer', ' wages', ' waste', ' watch', ' water', ' wealth', ' weapon', ' weather', ' weigh', ' welcome', ' wheat', ' wheel', ' where', ' whether', ' which', ' While', ' white', ' whole', ' willing', ' window', ' winter', ' withdraw', ' without', ' witness', ' woman', ' wonder', ' wonderful', ' world', ' worry', ' worse', ' worth', ' wound', ' wreck', ' wreckage', ' write', ' wrong', ' yellow', ' yesterday']
    t=random.randint(0,len(WordList))
    gameWord=WordList[t]
    lowMinCap=ord('a')-ord('A')
    for i in range(0,len(gameWord)):
        if(ord(gameWord[i])>=ord('a') and ord(gameWord[i])<=ord('z')):
            gameWord[i]=chr(ord(gameWord[i])-lowMinCap)
        if(gameWord[i]!=' ' and (gameWord[i]<ord('A') or gameWord[i]>ord('Z'))):
            del gameWord[i]
    gameDisplay=['__']*len(gameWord)
    return gameWord,lowMinCap,gameDisplay


def MultiPlayerHangman():
    [numOfPlayers,listOfPlayers,numOfGames,playerScore]=PlayerSetUp()
    gameOver=False
    for i in range(numOfGames):
        print('beginning game ',[i])
        [gameWord,lowMinCap,gameDisplay]=GameSetUp()
        while(gameOver==False):
            turn=TurnTracker(numOfPlayers,turn)
            guess=Guess(lowMinCap,gameWord, gameDisplay, playerScore)
            gameOver=PlayGame(listOfPlayers,turn,lowMinCap,gameWord,gameDisplay)
        print("Game", numOfGames,"over.")
    ShowEndScore(listOfPlayers,playerScore)


def PlayerSetUp():
    numOfPlayers=int(input("Enter Number of Players: "))
    listOfPlayers=[0]*numOfPlayers
    for i in range(numOfPlayers):
        listOfPlayers[i]=input(f"Enter name of player {i+1}: ")
    numOfGames=int(input("How many games would you like your challenge to have? "))
    print("Welcome:")
    playerScore=[0]*numOfPlayers
    return numOfPlayers,listOfPlayers, numOfGames,playerScore
    


def PlayGame(listOfPlayers,turn,lowMinCap,gameWord, gameDisplay):
    gameOver=True
    for i in range(0,len(gameWord)):
        if(gameWord[i]==guess):
            gameDisplay[i]=guess
            playerScore+=1
        if(gameDisplay[i]=='__'):
            gameOver=False
    return(gameOver)    


def HangmanDisplay(numOfPlayers,listOfPlayers,playerScore,gameDisplay,\
                   incorrectLetters,gameWord):
    for i in range(numOfPlayers):
        print(listOfPlayers[i], ': ', playerScore[i])
    print()
    for i in range(len(gameDisplay)):
        print(gameDisplay[i], end=" ")
    print()
    print(incorrectLetters)
    

def Guess(lowMinCap,gameWord, gameDisplay, playerScore):
    guess=input('{listOfPlayers[turn]}',"'s turn: Guess a letter: ")
    while(len(guess)!=1 or ord(guess)<ord('a') \
          or ord(guess)>ord('z') and ord(guess)<ord('A') \
          or ord(guess)>ord('Z')):
        guess=input('invalid answer: Guess a letter: ' )
    if(ord(guess)>ord('Z')):
        guess=chr(ord(guess)-lowMinCap)
    return guess

def TurnTracker(numOfPlayers,turn):
    if(turn==numOfPlayers):
        turn=0
    else:
        turn+=1
    return turn
    

def ShowEndScore(listOfPlayers,playerScores):
    for i in range(1,playerScores):
        x=playerScores[0]
        while(x>playerScores[i]):
            x+=1
        if(x<i):
            [temp1,temp2]=[playerScores[i],listOfPlayers[i]]
            [playerScores[i],listOfPlayers[i]]=\
                [playerScores[x],listOfPlayers[x]]
            [playerScores[x],listOfPlayers[x]]=\
                [playerScores[temp1],listOfPlayers[temp2]]
    print("Player", listOfPlayers[0],"wins!!!")
    print("Final score:",listOfPlayers[0], " " ,playerScores[0]," points"  )
    for i in range(1,listOfPlayers):
        print("            ",listOfPlayers[i], " " ,playerScores[i]," points")  
        




MultiPlayerHangman()