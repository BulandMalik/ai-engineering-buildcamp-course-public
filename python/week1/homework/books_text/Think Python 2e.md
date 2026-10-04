|     |               | Think      | Python    |
| --- | ------------- | ---------- | --------- |
| How | to Think Like | a Computer | Scientist |
2ndEdition,Version2.4.0

|     |               | Think      | Python    |
| --- | ------------- | ---------- | --------- |
| How | to Think Like | a Computer | Scientist |
2ndEdition,Version2.4.0
|     |     | Allen | Downey    |
| --- | --- | ----- | --------- |
|     |     | Green | Tea Press |
Needham,Massachusetts

Copyright©2015AllenDowney.
GreenTeaPress
9WashburnAve
NeedhamMA02492
Permission is granted to copy, distribute, and/or modify this document under the terms of the
CreativeCommonsAttribution-NonCommercial3.0UnportedLicense,whichisavailableathttp:
//creativecommons.org/licenses/by-nc/3.0/.
TheoriginalformofthisbookisLATEXsourcecode.CompilingthisLATEXsourcehastheeffectofgen-
eratingadevice-independentrepresentationofatextbook,whichcanbeconvertedtootherformats
andprinted.
TheLATEXsourceforthisbookisavailablefromhttp://www.thinkpython.com

Preface
The strange history of this book
InJanuary1999IwaspreparingtoteachanintroductoryprogrammingclassinJava. Ihad
taughtitthreetimesandIwasgettingfrustrated. Thefailurerateintheclasswastoohigh
and,evenforstudentswhosucceeded,theoveralllevelofachievementwastoolow.
OneoftheproblemsIsawwasthebooks. Theyweretoobig,withtoomuchunnecessary
detailaboutJava,andnotenoughhigh-levelguidanceabouthowtoprogram.Andtheyall
sufferedfromthetrapdooreffect: theywouldstartouteasy,proceedgradually,andthen
somewherearoundChapter5thebottomwouldfallout.Thestudentswouldgettoomuch
newmaterial,toofast,andIwouldspendtherestofthesemesterpickingupthepieces.
Twoweeksbeforethefirstdayofclasses,Idecidedtowritemyownbook. Mygoalswere:
• Keepitshort. Itisbetterforstudentstoread10pagesthannotread50pages.
• Be careful with vocabulary. I tried to minimize jargon and define each term at first
use.
• Buildgradually. Toavoidtrapdoors, Itookthemostdifficulttopicsandsplitthem
intoaseriesofsmallsteps.
• Focus on programming, not the programming language. I included the minimum
usefulsubsetofJavaandleftouttherest.
Ineededatitle,soonawhimIchoseHowtoThinkLikeaComputerScientist.
Myfirstversionwasrough,butitworked. Studentsdidthereading,andtheyunderstood
enough that I could spend class time on the hard topics, the interesting topics and (most
important)lettingthestudentspractice.
I released the book under the GNU Free Documentation License, which allows users to
copy,modify,anddistributethebook.
Whathappenednextisthecoolpart. JeffElkner,ahighschoolteacherinVirginia,adopted
mybookandtranslateditintoPython. Hesentmeacopyofhistranslation,andIhadthe
unusual experience of learning Python by reading my own book. As Green Tea Press, I
publishedthefirstPythonversionin2001.
In2003IstartedteachingatOlinCollegeandIgottoteachPythonforthefirsttime. The
contrast with Java was striking. Students struggled less, learned more, worked on more
interestingprojects,andgenerallyhadalotmorefun.

vi Chapter0. Preface
Since then I’ve continued to develop the book, correcting errors, improving some of the
examplesandaddingmaterial,especiallyexercises.
Theresultisthisbook,nowwiththelessgrandiosetitleThinkPython. Someofthechanges
are:
• Iaddedasectionaboutdebuggingattheendofeachchapter. Thesesectionspresent
general techniques for finding and avoiding bugs, and warnings about Python pit-
falls.
• Iaddedmoreexercises,rangingfromshorttestsofunderstandingtoafewsubstantial
projects. Mostexercisesincludealinktomysolution.
• Iaddedaseriesofcasestudies—longerexampleswithexercises,solutions,anddis-
cussion.
• Iexpandedthediscussionofprogramdevelopmentplansandbasicdesignpatterns.
• Iaddedappendicesaboutdebuggingandanalysisofalgorithms.
ThesecondeditionofThinkPythonhasthesenewfeatures:
• ThebookandallsupportingcodehavebeenupdatedtoPython3.
• I added a few sections, and more details on the web, to help beginners get started
runningPythoninabrowser,soyoudon’thavetodealwithinstallingPythonuntil
youwantto.
• ForChapter4.1Iswitchedfrommyownturtlegraphicspackage,calledSwampy,toa
morestandardPythonmodule,turtle,whichiseasiertoinstallandmorepowerful.
• I added a new chapter called “The Goodies”, which introduces some additional
Pythonfeaturesthatarenotstrictlynecessary,butsometimeshandy.
Ihopeyouenjoyworkingwiththisbook,andthatithelpsyoulearntoprogramandthink
likeacomputerscientist,atleastalittlebit.
AllenB.Downey
OlinCollege
Acknowledgments
Many thanks to Jeff Elkner, who translated my Java book into Python, which got this
projectstartedandintroducedmetowhathasturnedouttobemyfavoritelanguage.
ThanksalsotoChrisMeyers,whocontributedseveralsectionstoHowtoThinkLikeaCom-
puterScientist.
ThankstotheFreeSoftwareFoundationfordevelopingtheGNUFreeDocumentationLi-
cense, which helped make my collaboration with Jeff and Chris possible, and Creative
CommonsforthelicenseIamusingnow.

vii
ThankstotheeditorsatLuluwhoworkedonHowtoThinkLikeaComputerScientist.
ThankstotheeditorsatO’ReillyMediawhoworkedonThinkPython.
Thankstoallthestudentswhoworkedwithearlierversionsofthisbookandallthecon-
tributors(listedbelow)whosentincorrectionsandsuggestions.
Contributor List
Morethan100sharp-eyedandthoughtfulreadershavesentinsuggestionsandcorrections
overthepastfewyears. Theircontributions,andenthusiasmforthisproject,havebeena
hugehelp.
Ifyouhaveasuggestionorcorrection, pleasesendemailtofeedback@thinkpython.com.
If I make a change based on your feedback, I will add you to the contributor list (unless
youasktobeomitted).
Ifyouincludeatleastpartofthesentencetheerrorappearsin,thatmakesiteasyformeto
search. Pageandsectionnumbersarefine,too,butnotquiteaseasytoworkwith. Thanks!
• LloydHughAllensentinacorrectiontoSection8.4.
• YvonBouliannesentinacorrectionofasemanticerrorinChapter5.
• FredBremmersubmittedacorrectioninSection2.1.
• Jonah Cohen wrote the Perl scripts to convert the LaTeX source for this book into beautiful
HTML.
• Michael Conlon sent in a grammar correction in Chapter 2 and an improvement in style in
Chapter1,andheinitiateddiscussiononthetechnicalaspectsofinterpreters.
• BenoîtGirardsentinacorrectiontoahumorousmistakeinSection5.6.
• CourtneyGleasonandKatherineSmithwrotehorsebet.py,whichwasusedasacasestudy
inanearlierversionofthebook.Theirprogramcannowbefoundonthewebsite.
• LeeHarrsubmittedmorecorrectionsthanwehaveroomtolisthere,andindeedheshouldbe
listedasoneoftheprincipaleditorsofthetext.
• JamesKaylinisastudentusingthetext.Hehassubmittednumerouscorrections.
• DavidKershawfixedthebrokencatTwicefunctioninSection3.10.
• EddieLamhassentinnumerouscorrectionstoChapters1,2,and3.HealsofixedtheMakefile
sothatitcreatesanindexthefirsttimeitisrunandhelpedussetupaversioningscheme.
• Man-YongLeesentinacorrectiontotheexamplecodeinSection2.4.
• DavidMayopointedoutthattheword“unconsciously"inChapter1neededtobechangedto
“subconsciously".
• ChrisMcAloonsentinseveralcorrectionstoSections3.9and3.10.
• MatthewJ.Moelterhasbeenalong-timecontributorwhosentinnumerouscorrectionsand
suggestionstothebook.

viii Chapter0. Preface
• SimonDiconMontfordreportedamissingfunctiondefinitionandseveraltyposinChapter3.
HealsofounderrorsintheincrementfunctioninChapter13.
• JohnOuztscorrectedthedefinitionof“returnvalue"inChapter3.
• KevinParkssentinvaluablecommentsandsuggestionsastohowtoimprovethedistribution
ofthebook.
• DavidPoolsentinatypointheglossaryofChapter1,aswellaskindwordsofencouragement.
• MichaelSchmittsentinacorrectiontothechapteronfilesandexceptions.
• RobinShawpointedoutanerrorinSection13.1,wheretheprintTimefunctionwasusedinan
examplewithoutbeingdefined.
• PaulSleighfoundanerrorinChapter7andabuginJonahCohen’sPerlscriptthatgenerates
HTMLfromLaTeX.
• CraigT.SnydalistestingthetextinacourseatDrewUniversity. Hehascontributedseveral
valuablesuggestionsandcorrections.
• IanThomasandhisstudentsareusingthetextinaprogrammingcourse.Theyarethefirstones
totestthechaptersinthelatterhalfofthebook,andtheyhavemadenumerouscorrectionsand
suggestions.
• KeithVerheydensentinacorrectioninChapter3.
• PeterWinstanleyletusknowaboutalongstandingerrorinourLatininChapter3.
• ChrisWrobelmadecorrectionstothecodeinthechapteronfileI/Oandexceptions.
• MosheZadkahasmadeinvaluablecontributionstothisproject.Inadditiontowritingthefirst
draftofthechapteronDictionaries,heprovidedcontinualguidanceintheearlystagesofthe
book.
• ChristophZwerschkesentseveralcorrectionsandpedagogicsuggestions,andexplainedthe
differencebetweengleichandselbe.
• JamesMayersentusawholeslewofspellingandtypographicalerrors,includingtwointhe
contributorlist.
• HaydenMcAfeecaughtapotentiallyconfusinginconsistencybetweentwoexamples.
• AngelArnalispartofaninternationalteamoftranslatorsworkingontheSpanishversionof
thetext.HehasalsofoundseveralerrorsintheEnglishversion.
• TauhidulHoqueandLexBerezhnycreatedtheillustrationsinChapter1andimprovedmany
oftheotherillustrations.
• Dr. MicheleAlzettacaughtanerrorinChapter8andsentsomeinterestingpedagogiccom-
mentsandsuggestionsaboutFibonacciandOldMaid.
• AndyMitchellcaughtatypoinChapter1andabrokenexampleinChapter2.
• KalinHarveysuggestedaclarificationinChapter7andcaughtsometypos.
• ChristopherP.SmithcaughtseveraltyposandhelpedusupdatethebookforPython2.2.
• DavidHutchinscaughtatypointheForeword.
• GregorLinglisteachingPythonatahighschoolinVienna,Austria. HeisworkingonaGer-
mantranslationofthebook,andhecaughtacoupleofbaderrorsinChapter5.

ix
• JuliePeterscaughtatypointhePreface.
• FlorinOprinasentinanimprovementinmakeTime,acorrectioninprintTime,andanicetypo.
• D.J.WebresuggestedaclarificationinChapter3.
• KenfoundafistfuloferrorsinChapters8,9and11.
• IvoWevercaughtatypoinChapter5andsuggestedaclarificationinChapter3.
• CurtisYankosuggestedaclarificationinChapter2.
• BenLogansentinanumberoftyposandproblemswithtranslatingthebookintoHTML.
• JasonArmstrongsawthemissingwordinChapter2.
• LouisCordiernoticedaspotinChapter16wherethecodedidn’tmatchthetext.
• BrianCainsuggestedseveralclarificationsinChapters2and3.
• RobBlacksentinapasselofcorrections,includingsomechangesforPython2.2.
• Jean-PhilippeReyatÉcoleCentraleParissentanumberofpatches,includingsomeupdates
forPython2.2andotherthoughtfulimprovements.
• JasonMaderatGeorgeWashingtonUniversitymadeanumberofusefulsuggestionsandcor-
rections.
• JanGundtofte-Bruunremindedusthat“aerror”isanerror.
• AbelDavidandAlexisDinnoremindedusthatthepluralof“matrix”is“matrices”,not“ma-
trixes”.Thiserrorwasinthebookforyears,buttworeaderswiththesameinitialsreportedit
onthesameday.Weird.
• CharlesThayerencouragedustogetridofthesemi-colonswehadputattheendsofsome
statementsandtocleanupouruseof“argument”and“parameter”.
• RogerSperbergpointedoutatwistedpieceoflogicinChapter3.
• SamBullpointedoutaconfusingparagraphinChapter2.
• AndrewCheungpointedouttwoinstancesof“usebeforedef”.
• C.CoreyCapelspottedthemissingwordintheThirdTheoremofDebuggingandatypoin
Chapter4.
• AlessandrahelpedclearupsomeTurtleconfusion.
• WimChampagnefoundabrain-oinadictionaryexample.
• DouglasWrightpointedoutaproblemwithfloordivisioninarc.
• JaredSpindorfoundsomejetsamattheendofasentence.
• LinPeihengsentanumberofveryhelpfulsuggestions.
• RayHagtvedtsentintwoerrorsandanot-quite-error.
• TorstenHübschpointedoutaninconsistencyinSwampy.
• IngaPetuhhovcorrectedanexampleinChapter14.
• ArneBabenhauserheidesentseveralhelpfulcorrections.

x Chapter0. Preface
• MarkE.Casidaisisgoodatspottingrepeatedwords.
• ScottTylerfilledinathatwasmissing.Andthensentinaheapofcorrections.
• GordonShephardsentinseveralcorrections,allinseparateemails.
• AndrewTurnerspottedanerrorinChapter8.
• AdamHobartfixedaproblemwithfloordivisioninarc.
• DarylHammondandSarahZimmermanpointedoutthatIservedupmath.pitooearly. And
Zimspottedatypo.
• GeorgeSassfoundabuginaDebuggingsection.
• BrianBinghamsuggestedExercise11.5.
• LeahEngelbert-FentonpointedoutthatIusedtupleasavariablename,contrarytomyown
advice.Andthenfoundabunchoftyposanda“usebeforedef”.
• JoeFunkespottedatypo.
• Chao-chaoChenfoundaninconsistencyintheFibonacciexample.
• JeffPaineknowsthedifferencebetweenspaceandspam.
• LubosPintessentinatypo.
• GreggLindandAbigailHeithoffsuggestedExercise14.3.
• MaxHailperinhassentinanumberofcorrectionsandsuggestions.Maxisoneoftheauthors
oftheextraordinaryConcreteAbstractions,whichyoumightwanttoreadwhenyouaredone
withthisbook.
• ChotipatPornavalaifoundanerrorinanerrormessage.
• StanislawAntolsentalistofveryhelpfulsuggestions.
• EricPashmansentanumberofcorrectionsforChapters4–11.
• MiguelAzevedofoundsometypos.
• JianhuaLiusentinalonglistofcorrections.
• NickKingfoundamissingword.
• MartinZuthersentalonglistofsuggestions.
• AdamZimmermanfoundaninconsistencyinmyinstanceofan“instance”andseveralother
errors.
• RatnakarTiwarisuggestedafootnoteexplainingdegeneratetriangles.
• AnuragGoelsuggestedanothersolutionforis_abecedarianandsentsomeadditionalcorrec-
tions.AndheknowshowtospellJaneAusten.
• KelliKratzerspottedoneofthetypos.
• MarkGriffithspointedoutaconfusingexampleinChapter3.
• RoydanOngiefoundanerrorinmyNewton’smethod.
• PatrykWolowiechelpedmewithaproblemintheHTMLversion.

xi
• MarkChonofskytoldmeaboutanewkeywordinPython3.
• RussellColemanhelpedmewithmygeometry.
• NamNguyenfoundatypoandpointedoutthatIusedtheDecoratorpatternbutdidn’tmen-
tionitbyname.
• StéphaneMorinsentinseveralcorrectionsandsuggestions.
• PaulStoopcorrectedatypoinuses_only.
• EricBronnerpointedoutaconfusioninthediscussionoftheorderofoperations.
• AlexandrosGezerlissetanewstandardforthenumberandqualityofsuggestionshesubmit-
ted.Wearedeeplygrateful!
• GrayThomasknowshisrightfromhisleft.
• GiovanniEscobarSosasentalonglistofcorrectionsandsuggestions.
• DanielNeilsoncorrectedanerrorabouttheorderofoperations.
• WillMcGinnispointedoutthatpolylinewasdefineddifferentlyintwoplaces.
• FrankHeckerpointedoutanexercisethatwasunder-specified,andsomebrokenlinks.
• AnimeshBhelpedmecleanupaconfusingexample.
• MartinCaspersenfoundtworound-offerrors.
• GregorUlmsentseveralcorrectionsandsuggestions.
• DimitriosTsirigkassuggestedIclarifyanexercise.
• CarlosTafursentapageofcorrectionsandsuggestions.
• MartinNordslettenfoundabuginanexercisesolution.
• SvenHoexterpointedoutthatavariablenamedinputshadowsabuild-infunction.
• StephenGregorypointedouttheproblemwithcmpinPython3.
• IshwarBhatcorrectedmystatementofFermat’slasttheorem.
• Andrea Zanella translated the book into Italian, and sent a number of corrections along the
way.
• Many,manythankstoMelissaLewisandLucianoRamalhoforexcellentcommentsandsug-
gestionsonthesecondedition.
• ThankstoHarryPercivalfromPythonAnywhereforhishelpgettingpeoplestartedrunning
Pythoninabrowser.
• XavierVanAubelmadeseveralusefulcorrectionsinthesecondedition.
• WilliamMurraycorrectedmydefinitionoffloordivision.
• PerStarbäckbroughtmeuptodateonuniversalnewlinesinPython3.
• LaurentRosenfeldandMihaelaRotarutranslatedthisbookintoFrench. Alongtheway,they
sentmanycorrectionsandsuggestions.
Inaddition,peoplewhospottedtyposormadecorrectionsincludeCzeslawCzapla,DaleWil-
son,FrancescoCarloCimini,RichardFursa,BrianMcGhie,LokeshKumarMakani,Matthew
Shultz, Viet Le, Victor Simeone, Lars O.D. Christensen, Swarup Sahoo, Alix Etienne, Kuang
He,WeiHuang,KarenBarber,andEricRansom.

| xii | Chapter0. | Preface |
| --- | --------- | ------- |

Contents
Preface v
1 Thewayoftheprogram 1
1.1 Whatisaprogram? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 RunningPython . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Thefirstprogram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Arithmeticoperators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.5 Valuesandtypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6 Formalandnaturallanguages . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.7 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.8 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.9 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2 Variables,expressionsandstatements 9
2.1 Assignmentstatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2 Variablenames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3 Expressionsandstatements . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Scriptmode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.5 Orderofoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.6 Stringoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.7 Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.8 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.9 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.10 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

xiv Contents
3 Functions 17
3.1 Functioncalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.2 Mathfunctions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3 Composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.4 Addingnewfunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.5 Definitionsanduses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6 Flowofexecution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.7 Parametersandarguments . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.8 Variablesandparametersarelocal . . . . . . . . . . . . . . . . . . . . . . . 22
3.9 Stackdiagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.10 Fruitfulfunctionsandvoidfunctions . . . . . . . . . . . . . . . . . . . . . . 24
3.11 Whyfunctions? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.12 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.13 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.14 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4 Casestudy: interfacedesign 29
4.1 Theturtlemodule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.2 Simplerepetition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.3 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.4 Encapsulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.5 Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.6 Interfacedesign . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.7 Refactoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.8 Adevelopmentplan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.9 docstring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.10 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.11 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.12 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

Contents xv
5 Conditionalsandrecursion 39
5.1 Floordivisionandmodulus . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.2 Booleanexpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.3 Logicaloperators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.4 Conditionalexecution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.5 Alternativeexecution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.6 Chainedconditionals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.7 Nestedconditionals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.8 Recursion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.9 Stackdiagramsforrecursivefunctions . . . . . . . . . . . . . . . . . . . . . 44
5.10 Infiniterecursion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.11 Keyboardinput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.12 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.13 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
5.14 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6 Fruitfulfunctions 51
6.1 Returnvalues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.2 Incrementaldevelopment . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.3 Composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.4 Booleanfunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.5 Morerecursion. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
6.6 Leapoffaith . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
6.7 Onemoreexample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
6.8 Checkingtypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
6.9 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
6.10 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
6.11 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

xvi Contents
7 Iteration 63
7.1 Reassignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7.2 Updatingvariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7.3 Thewhilestatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7.4 break . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
7.5 Squareroots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
7.6 Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
7.7 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.8 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7.9 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
8 Strings 71
8.1 Astringisasequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
8.2 len . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
8.3 Traversalwithaforloop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
8.4 Stringslices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
8.5 Stringsareimmutable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.6 Searching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.7 Loopingandcounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
8.8 Stringmethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
8.9 Theinoperator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
8.10 Stringcomparison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
8.11 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
8.12 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
8.13 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
9 Casestudy: wordplay 83
9.1 Readingwordlists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
9.2 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
9.3 Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
9.4 Loopingwithindices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
9.5 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
9.6 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
9.7 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

Contents xvii
10 Lists 89
10.1 Alistisasequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
10.2 Listsaremutable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
10.3 Traversingalist . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.4 Listoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.5 Listslices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.6 Listmethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
10.7 Map,filterandreduce . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.8 Deletingelements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
10.9 Listsandstrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
10.10 Objectsandvalues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
10.11 Aliasing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
10.12 Listarguments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.13 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.14 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
10.15 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
11 Dictionaries 103
11.1 Adictionaryisamapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
11.2 Dictionaryasacollectionofcounters . . . . . . . . . . . . . . . . . . . . . . 104
11.3 Loopinganddictionaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
11.4 Reverselookup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
11.5 Dictionariesandlists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
11.6 Memos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
11.7 Globalvariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
11.8 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
11.9 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
11.10 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

xviii Contents
12 Tuples 115
12.1 Tuplesareimmutable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
12.2 Tupleassignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
12.3 Tuplesasreturnvalues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
12.4 Variable-lengthargumenttuples . . . . . . . . . . . . . . . . . . . . . . . . 118
12.5 Listsandtuples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
12.6 Dictionariesandtuples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
12.7 Sequencesofsequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
12.8 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
12.9 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
12.10 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
13 Casestudy: datastructureselection 125
13.1 Wordfrequencyanalysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
13.2 Randomnumbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.3 Wordhistogram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
13.4 Mostcommonwords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
13.5 Optionalparameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
13.6 Dictionarysubtraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
13.7 Randomwords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
13.8 Markovanalysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
13.9 Datastructures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
13.10 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
13.11 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
13.12 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
14 Files 137
14.1 Persistence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
14.2 Readingandwriting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
14.3 Formatoperator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
14.4 Filenamesandpaths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
14.5 Catchingexceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

Contents xix
14.6 Databases. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
14.7 Pickling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
14.8 Pipes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
14.9 Writingmodules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
14.10 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
14.11 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
14.12 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
15 Classesandobjects 147
15.1 Programmer-definedtypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
15.2 Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
15.3 Rectangles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
15.4 Instancesasreturnvalues . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
15.5 Objectsaremutable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
15.6 Copying . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
15.7 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
15.8 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
15.9 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
16 Classesandfunctions 155
16.1 Time. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
16.2 Purefunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
16.3 Modifiers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
16.4 Prototypingversusplanning . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
16.5 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
16.6 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
16.7 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
17 Classesandmethods 161
17.1 Object-orientedfeatures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
17.2 Printingobjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
17.3 Anotherexample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163

xx Contents
17.4 Amorecomplicatedexample . . . . . . . . . . . . . . . . . . . . . . . . . . 164
17.5 Theinitmethod . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
17.6 The__str__method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
17.7 Operatoroverloading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
17.8 Type-baseddispatch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
17.9 Polymorphism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
17.10 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
17.11 Interfaceandimplementation . . . . . . . . . . . . . . . . . . . . . . . . . . 169
17.12 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
17.13 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
18 Inheritance 171
18.1 Cardobjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
18.2 Classattributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
18.3 Comparingcards . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
18.4 Decks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
18.5 Printingthedeck . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
18.6 Add,remove,shuffleandsort . . . . . . . . . . . . . . . . . . . . . . . . . . 175
18.7 Inheritance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
18.8 Classdiagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
18.9 Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
18.10 Dataencapsulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
18.11 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
18.12 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
19 TheGoodies 183
19.1 Conditionalexpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
19.2 Listcomprehensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
19.3 Generatorexpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
19.4 anyandall . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
19.5 Sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
19.6 Counters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187

Contents xxi
19.7 defaultdict . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
19.8 Namedtuples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
19.9 Gatheringkeywordargs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
19.10 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
19.11 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
A Debugging 193
A.1 Syntaxerrors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
A.2 Runtimeerrors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
A.3 Semanticerrors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
B AnalysisofAlgorithms 201
B.1 Orderofgrowth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
B.2 AnalysisofbasicPythonoperations . . . . . . . . . . . . . . . . . . . . . . 204
B.3 Analysisofsearchalgorithms . . . . . . . . . . . . . . . . . . . . . . . . . . 205
B.4 Hashtables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
B.5 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209

xxii Contents

Chapter 1
The way of the program
Thegoalofthisbookistoteachyoutothinklikeacomputerscientist. Thiswayofthink-
ing combinessome ofthe bestfeatures of mathematics, engineering, andnatural science.
Like mathematicians, computer scientists use formal languages to denote ideas (specifi-
callycomputations). Likeengineers,theydesignthings,assemblingcomponentsintosys-
temsandevaluatingtradeoffsamongalternatives. Likescientists,theyobservethebehav-
iorofcomplexsystems,formhypotheses,andtestpredictions.
Thesinglemostimportantskillforacomputerscientistisproblemsolving. Problemsolv-
ingmeanstheabilitytoformulateproblems,thinkcreativelyaboutsolutions,andexpress
asolutionclearlyandaccurately. Asitturnsout,theprocessoflearningtoprogramisan
excellentopportunitytopracticeproblem-solvingskills. That’swhythischapteriscalled,
“Thewayoftheprogram”.
Ononelevel,youwillbelearningtoprogram,ausefulskillbyitself.Onanotherlevel,you
willuseprogrammingasameanstoanend. Aswegoalong,thatendwillbecomeclearer.
1.1 What is a program?
Aprogramisasequenceofinstructionsthatspecifieshowtoperformacomputation. The
computationmightbesomethingmathematical, suchassolvingasystemofequationsor
findingtherootsofapolynomial,butitcanalsobeasymboliccomputation,suchassearch-
ingandreplacingtextinadocumentorsomethinggraphical,likeprocessinganimageor
playingavideo.
Thedetailslookdifferentindifferentlanguages,butafewbasicinstructionsappearinjust
abouteverylanguage:
input: Getdatafromthekeyboard,afile,thenetwork,orsomeotherdevice.
output: Displaydataonthescreen,saveitinafile,senditoverthenetwork,etc.
math: Performbasicmathematicaloperationslikeadditionandmultiplication.
conditionalexecution: Checkforcertainconditionsandruntheappropriatecode.

2 Chapter1. Thewayoftheprogram
repetition: Performsomeactionrepeatedly,usuallywithsomevariation.
Believe it or not, that’s pretty much all there is to it. Every program you’ve ever used,
no matter how complicated, is made up of instructions that look pretty much like these.
So you can think of programming as the process of breaking a large, complex task into
smaller and smaller subtasks until the subtasks are simple enough to be performed with
oneofthesebasicinstructions.
1.2 Running Python
One of the challenges of getting started with Python is that you might have to install
Python and related software on your computer. If you are familiar with your operating
system, and especially if you are comfortable with the command-line interface, you will
havenotroubleinstallingPython. Butforbeginners, itcanbepainfultolearnaboutsys-
temadministrationandprogrammingatthesametime.
Toavoidthatproblem,IrecommendthatyoustartoutrunningPythoninabrowser. Later,
whenyouarecomfortablewithPython,I’llmakesuggestionsforinstallingPythononyour
computer.
There are a number of web pages you can use to run Python. If you already have a fa-
vorite,goaheadanduseit. OtherwiseIrecommendPythonAnywhere. Iprovidedetailed
instructionsforgettingstartedathttp://tinyurl.com/thinkpython2e.
TherearetwoversionsofPython,calledPython2andPython3. Theyareverysimilar,so
ifyoulearnone,itiseasytoswitchtotheother.Infact,thereareonlyafewdifferencesyou
will encounter as abeginner. Thisbook iswritten for Python3, butI includesome notes
aboutPython2.
The Python interpreter is a program that reads and executes Python code. Depending
onyourenvironment,youmightstarttheinterpreterbyclickingonanicon,orbytyping
pythononacommandline. Whenitstarts,youshouldseeoutputlikethis:
Python 3.4.0 (default, Jun 19 2015, 14:20:21)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
Thefirstthreelinescontaininformationabouttheinterpreterandtheoperatingsystemit’s
runningon,soitmightbedifferentforyou.Butyoushouldcheckthattheversionnumber,
whichis3.4.0inthisexample,beginswith3,whichindicatesthatyouarerunningPython
3. Ifitbeginswith2,youarerunning(youguessedit)Python2.
Thelastlineisapromptthatindicatesthattheinterpreterisreadyforyoutoentercode. If
youtypealineofcodeandhitEnter,theinterpreterdisplaystheresult:
>>> 1 + 1
2
Nowyou’rereadytogetstarted. Fromhereon, Iassumethatyouknowhowtostartthe
Pythoninterpreterandruncode.

1.3. Thefirstprogram 3
1.3 The first program
Traditionally,thefirstprogramyouwriteinanewlanguageiscalled“Hello,World!” be-
causeallitdoesisdisplaythewords“Hello,World!”. InPython,itlookslikethis:
>>> print('Hello, World!')
This is an example of a print statement, although it doesn’t actually print anything on
paper. Itdisplaysaresultonthescreen. Inthiscase,theresultisthewords
Hello, World!
The quotation marks in the program mark the beginning and end of the text to be dis-
played;theydon’tappearintheresult.
Theparenthesesindicatethatprintisafunction. We’llgettofunctionsinChapter3.
In Python 2, the print statement is slightly different; it is not a function, so it doesn’t use
parentheses.
>>> print 'Hello, World!'
Thisdistinctionwillmakemoresensesoon,butthat’senoughtogetstarted.
1.4 Arithmetic operators
After “Hello, World”, the next step is arithmetic. Python provides operators, which are
specialsymbolsthatrepresentcomputationslikeadditionandmultiplication.
The operators +, -, and * perform addition, subtraction, and multiplication, as in the fol-
lowingexamples:
>>> 40 + 2
42
>>> 43 - 1
42
>>> 6 * 7
42
Theoperator/performsdivision:
>>> 84 / 2
42.0
Youmightwonderwhytheresultis42.0insteadof42. I’llexplaininthenextsection.
Finally,theoperator**performsexponentiation;thatis,itraisesanumbertoapower:
>>> 6**2 + 6
42
Insomeotherlanguages,^isusedforexponentiation,butinPythonitisabitwiseoperator
calledXOR.Ifyouarenotfamiliarwithbitwiseoperators,theresultwillsurpriseyou:
>>> 6 ^ 2
4
Iwon’tcoverbitwiseoperatorsinthisbook,butyoucanreadaboutthemathttp://wiki.
python.org/moin/BitwiseOperators.

4 Chapter1. Thewayoftheprogram
1.5 Values and types
Avalueisoneofthebasicthingsaprogramworkswith, likealetteroranumber. Some
valueswehaveseensofarare2,42.0,and'Hello, World!'.
Thesevaluesbelongtodifferenttypes:2isaninteger,42.0isafloating-pointnumber,and
'Hello, World!'isastring,so-calledbecausethelettersitcontainsarestrungtogether.
Ifyouarenotsurewhattypeavaluehas,theinterpretercantellyou:
>>> type(2)
<class 'int'>
>>> type(42.0)
<class 'float'>
>>> type('Hello, World!')
<class 'str'>
Intheseresults,theword“class”isusedinthesenseofacategory;atypeisacategoryof
values.
Notsurprisingly,integersbelongtothetypeint,stringsbelongtostrandfloating-point
numbersbelongtofloat.
Whataboutvalueslike'2'and'42.0'? Theylooklikenumbers,buttheyareinquotation
markslikestrings.
>>> type('2')
<class 'str'>
>>> type('42.0')
<class 'str'>
They’restrings.
When you type a large integer, you might be tempted to use commas between groups of
digits,asin1,000,000. ThisisnotalegalintegerinPython,butitislegal:
>>> 1,000,000
(1, 0, 0)
That’s not what we expected at all! Python interprets 1,000,000 as a comma-separated
sequenceofintegers. We’lllearnmoreaboutthiskindofsequencelater.
1.6 Formal and natural languages
Naturallanguagesarethelanguagespeoplespeak,suchasEnglish,Spanish,andFrench.
They were not designed by people (although people try to impose some order on them);
theyevolvednaturally.
Formallanguagesarelanguagesthataredesignedbypeopleforspecificapplications. For
example, the notation that mathematicians use is a formal language that is particularly
goodatdenotingrelationshipsamongnumbersandsymbols. Chemistsuseaformallan-
guagetorepresentthechemicalstructureofmolecules. Andmostimportantly:
Programming languages are formal languages that have been designed to
expresscomputations.

1.6. Formalandnaturallanguages 5
Formallanguagestendtohavestrictsyntaxrulesthatgovernthestructureofstatements.
For example, in mathematics the statement 3+3 = 6 has correct syntax, but 3+ = 3$6
doesnot. InchemistryH Oisasyntacticallycorrectformula,but Zzisnot.
2 2
Syntaxrulescomeintwoflavors,pertainingtotokensandstructure. Tokensarethebasic
elements of the language, such as words, numbers, and chemical elements. One of the
problems with 3+ = 3$6 is that $ is not a legal token in mathematics (at least as far as I
know). Similarly, ZzisnotlegalbecausethereisnoelementwiththeabbreviationZz.
2
The second type of syntax rule pertains to the way tokens are combined. The equation
3+/3 is illegal because even though + and / are legal tokens, you can’t have one right
aftertheother.Similarly,inachemicalformulathesubscriptcomesaftertheelementname,
notbefore.
Thisis@well-structuredEngli$hsentencewithinvalidt*kensinit. Thissentenceallvalid
tokenshas,butinvalidstructurewith.
When you read a sentence in English or a statement in a formal language, you have to
figureoutthestructure(althoughinanaturallanguageyoudothissubconsciously). This
processiscalledparsing.
Although formal and natural languages have many features in common—tokens, struc-
ture,andsyntax—therearesomedifferences:
ambiguity: Naturallanguagesarefullofambiguity,whichpeopledealwithbyusingcon-
textualcluesandotherinformation. Formallanguagesaredesignedtobenearlyor
completelyunambiguous,whichmeansthatanystatementhasexactlyonemeaning,
regardlessofcontext.
redundancy: In order to make up for ambiguity and reduce misunderstandings, natural
languages employ lots of redundancy. As a result, they are often verbose. Formal
languagesarelessredundantandmoreconcise.
literalness: Natural languages are full of idiom and metaphor. If I say, “The penny
dropped”,thereisprobablynopennyandnothingdropping(thisidiommeansthat
someoneunderstoodsomethingafteraperiodofconfusion).Formallanguagesmean
exactlywhattheysay.
Becauseweallgrowupspeakingnaturallanguages,itissometimeshardtoadjusttofor-
mallanguages. Thedifferencebetweenformalandnaturallanguageislikethedifference
betweenpoetryandprose,butmoreso:
Poetry: Wordsareusedfortheirsoundsaswellasfortheirmeaning,andthewholepoem
togethercreatesaneffectoremotionalresponse. Ambiguityisnotonlycommonbut
oftendeliberate.
Prose: Theliteralmeaningofwordsismoreimportant,andthestructurecontributesmore
meaning. Proseismoreamenabletoanalysisthanpoetrybutstilloftenambiguous.
Programs: The meaning of a computer program is unambiguous and literal, and can be
understoodentirelybyanalysisofthetokensandstructure.

6 Chapter1. Thewayoftheprogram
Formallanguagesaremoredensethannaturallanguages,soittakeslongertoreadthem.
Also,thestructureisimportant,soitisnotalwaysbesttoreadfromtoptobottom,leftto
right. Instead, learntoparsetheprogramin your head, identifyingthe tokens andinter-
pretingthestructure. Finally,thedetailsmatter. Smallerrorsinspellingandpunctuation,
whichyoucangetawaywithinnaturallanguages,canmakeabigdifferenceinaformal
language.
1.7 Debugging
Programmersmakemistakes. Forwhimsicalreasons,programmingerrorsarecalledbugs
andtheprocessoftrackingthemdowniscalleddebugging.
Programming, and especially debugging, sometimes brings out strong emotions. If you
arestrugglingwithadifficultbug,youmightfeelangry,despondent,orembarrassed.
Thereisevidencethatpeoplenaturallyrespondtocomputersasiftheywerepeople.When
theyworkwell,wethinkofthemasteammates,andwhentheyareobstinateorrude,we
respond to them the same way we respond to rude, obstinate people (Reeves and Nass,
The Media Equation: How People Treat Computers, Television, and New Media Like Real People
andPlaces).
Preparingforthesereactionsmighthelpyoudealwiththem. Oneapproachistothinkof
thecomputerasanemployeewithcertainstrengths,likespeedandprecision,andpartic-
ularweaknesses,likelackofempathyandinabilitytograspthebigpicture.
Yourjobistobeagoodmanager:findwaystotakeadvantageofthestrengthsandmitigate
theweaknesses. Andfindwaystouseyouremotionstoengagewiththeproblem,without
lettingyourreactionsinterferewithyourabilitytoworkeffectively.
Learningtodebugcanbefrustrating,butitisavaluableskillthatisusefulformanyactiv-
itiesbeyondprogramming. Attheendofeachchapterthereisasection,likethisone,with
mysuggestionsfordebugging. Ihopetheyhelp!
1.8 Glossary
problemsolving: Theprocessofformulatingaproblem,findingasolution,andexpress-
ingit.
high-levellanguage: AprogramminglanguagelikePythonthatisdesignedtobeeasyfor
humanstoreadandwrite.
low-levellanguage: Aprogramminglanguagethatisdesignedtobeeasyforacomputer
torun;alsocalled“machinelanguage”or“assemblylanguage”.
portability: Apropertyofaprogramthatcanrunonmorethanonekindofcomputer.
interpreter: Aprogramthatreadsanotherprogramandexecutesit
prompt: Characters displayed by the interpreter to indicate that it is ready to take input
fromtheuser.
program: Asetofinstructionsthatspecifiesacomputation.

1.9. Exercises 7
printstatement: An instruction that causes the Python interpreter to display a value on
thescreen.
operator: A special symbol that represents a simple computation like addition, multipli-
cation,orstringconcatenation.
value: Oneofthebasicunitsofdata,likeanumberorstring,thataprogrammanipulates.
type: Acategoryofvalues. Thetypeswehaveseensofarareintegers(typeint),floating-
pointnumbers(typefloat),andstrings(typestr).
integer: Atypethatrepresentswholenumbers.
floating-point: Atypethatrepresentsnumberswithfractionalparts.
string: Atypethatrepresentssequencesofcharacters.
naturallanguage: Anyoneofthelanguagesthatpeoplespeakthatevolvednaturally.
formallanguage: Any one of the languages that people have designed for specific pur-
poses,suchasrepresentingmathematicalideasorcomputerprograms;allprogram-
minglanguagesareformallanguages.
token: One of the basic elements of the syntactic structure of a program, analogous to a
wordinanaturallanguage.
syntax: Therulesthatgovernthestructureofaprogram.
parse: Toexamineaprogramandanalyzethesyntacticstructure.
bug: Anerrorinaprogram.
debugging: Theprocessoffindingandcorrectingbugs.
1.9 Exercises
Exercise 1.1. It is a good idea to read this book in front of a computer so you can try out the
examplesasyougo.
Wheneveryouareexperimentingwithanewfeature,youshouldtrytomakemistakes.Forexample,
inthe“Hello,world!” program,whathappensifyouleaveoutoneofthequotationmarks? Whatif
youleaveoutboth? Whatifyouspellprintwrong?
Thiskindofexperimenthelpsyourememberwhatyouread;italsohelpswhenyouareprogramming,
because you get to know what the error messages mean. It is better to make mistakes now and on
purposethanlaterandaccidentally.
1. Inaprintstatement,whathappensifyouleaveoutoneoftheparentheses,orboth?
2. Ifyouaretryingtoprintastring,whathappensifyouleaveoutoneofthequotationmarks,
orboth?
3. Youcanuseaminussigntomakeanegativenumberlike-2. Whathappensifyouputaplus
signbeforeanumber? Whatabout2++2?

8 Chapter1. Thewayoftheprogram
4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python?
Whatabout011?
5. Whathappensifyouhavetwovalueswithnooperatorbetweenthem?
Exercise1.2. StartthePythoninterpreteranduseitasacalculator.
1. Howmanysecondsaretherein42minutes42seconds?
2. Howmanymilesaretherein10kilometers? Hint: thereare1.61kilometersinamile.
3. Ifyouruna10kilometerracein42minutes42seconds,whatisyouraveragepace(timeper
mileinminutesandseconds)? Whatisyouraveragespeedinmilesperhour?

| Chapter    | 2   |             |     |     |
| ---------- | --- | ----------- | --- | --- |
| Variables, |     | expressions |     | and |
statements
Oneofthemostpowerfulfeaturesofaprogramminglanguageistheabilitytomanipulate
| variables.     | Avariableisanamethatreferstoavalue. |            |     |     |
| -------------- | ----------------------------------- | ---------- | --- | --- |
| 2.1 Assignment |                                     | statements |     |     |
Anassignmentstatementcreatesanewvariableandgivesitavalue:
| >>> message | = 'And             | now for something | completely | different' |
| ----------- | ------------------ | ----------------- | ---------- | ---------- |
| >>> n = 17  |                    |                   |            |            |
| >>> pi =    | 3.1415926535897932 |                   |            |            |
Thisexamplemakesthreeassignments. Thefirstassignsastringtoanewvariablenamed
message;thesecondgivestheinteger17ton;thethirdassignsthe(approximate)valueof
πtopi.
Acommonwaytorepresentvariablesonpaperistowritethenamewithanarrowpointing
toitsvalue. Thiskindoffigureiscalledastatediagrambecauseitshowswhatstateeach
ofthevariablesisin(thinkofitasthevariable’sstateofmind). Figure2.1showstheresult
ofthepreviousexample.
| 2.2 Variable | names |     |     |     |
| ------------ | ----- | --- | --- | --- |
Programmersgenerallychoosenamesfortheirvariablesthataremeaningful—theydocu-
mentwhatthevariableisusedfor.
|     | message | ’And now for something completely different’ |     |     |
| --- | ------- | -------------------------------------------- | --- | --- |
n 17
pi 3.1415926535897932
|     |     | Figure2.1: | Statediagram. |     |
| --- | --- | ---------- | ------------- | --- |

| 10  |     |     | Chapter2. | Variables,expressionsandstatements |
| --- | --- | --- | --------- | ---------------------------------- |
Variablenamescanbeaslongasyoulike. Theycancontainbothlettersandnumbers,but
theycan’tbeginwithanumber. Itislegaltouseuppercaseletters,butitisconventionalto
useonlylowercaseforvariablesnames.
Theunderscorecharacter,_,canappearinaname.
Itisoftenusedinnameswithmultiple
words,suchasyour_nameorairspeed_of_unladen_swallow.
Ifyougiveavariableanillegalname,yougetasyntaxerror:
| >>> 76trombones | = 'big      | parade'     |          |     |
| --------------- | ----------- | ----------- | -------- | --- |
| SyntaxError:    | invalid     | syntax      |          |     |
| >>> more@       | = 1000000   |             |          |     |
| SyntaxError:    | invalid     | syntax      |          |     |
| >>> class       | = 'Advanced | Theoretical | Zymurgy' |     |
| SyntaxError:    | invalid     | syntax      |          |     |
76trombonesisillegalbecauseitbeginswithanumber. more@isillegalbecauseitcontains
| anillegalcharacter,@. |     | Butwhat’swrongwithclass? |     |     |
| --------------------- | --- | ------------------------ | --- | --- |
class
It turns out that is one of Python’s keywords. The interpreter uses keywords to
recognizethestructureoftheprogram,andtheycannotbeusedasvariablenames.
Python3hasthesekeywords:
| False  | class    | finally | is       | return |
| ------ | -------- | ------- | -------- | ------ |
| None   | continue | for     | lambda   | try    |
| True   | def      | from    | nonlocal | while  |
| and    | del      | global  | not      | with   |
| as     | elif     | if      | or       | yield  |
| assert | else     | import  | pass     |        |
| break  | except   | in      | raise    |        |
You don’t have to memorize this list. In most development environments, keywords are
displayedinadifferentcolor;ifyoutrytouseoneasavariablename,you’llknow.
| 2.3 Expressions |     | and statements |     |     |
| --------------- | --- | -------------- | --- | --- |
Anexpressionisacombinationofvalues,variables,andoperators. Avalueallbyitselfis
consideredanexpression,andsoisavariable,sothefollowingarealllegalexpressions:
>>> 42
42
>>> n
17
| >>> n + | 25  |     |     |     |
| ------- | --- | --- | --- | --- |
42
Whenyoutypeanexpressionattheprompt,theinterpreterevaluatesit,whichmeansthat
Inthisexample,nhasthevalue17andn + 25hasthe
itfindsthevalueoftheexpression.
value42.
A statement is a unit of code that has an effect, like creating a variable or displaying a
value.
| >>> n = | 17  |     |     |     |
| ------- | --- | --- | --- | --- |
>>> print(n)

2.4. Scriptmode 11
Thefirstlineisanassignmentstatementthatgivesavalueton. Thesecondlineisaprint
statementthatdisplaysthevalueofn.
Whenyoutypeastatement,theinterpreterexecutesit,whichmeansthatitdoeswhatever
thestatementsays. Ingeneral,statementsdon’thavevalues.
2.4 Script mode
So far we have run Python in interactive mode, which means that you interact directly
withtheinterpreter. Interactivemodeisagoodwaytogetstarted,butifyouareworking
withmorethanafewlinesofcode,itcanbeclumsy.
Thealternativeistosavecodeinafilecalledascriptandthenruntheinterpreterinscript
modetoexecutethescript. Byconvention,Pythonscriptshavenamesthatendwith.py.
If you know how to create and run a script on your computer, you are ready to go. Oth-
erwiseIrecommendusingPythonAnywhereagain. Ihavepostedinstructionsforrunning
inscriptmodeathttp://tinyurl.com/thinkpython2e.
BecausePythonprovidesbothmodes,youcantestbitsofcodeininteractivemodebefore
you put them in a script. But there are differences between interactive mode and script
modethatcanbeconfusing.
Forexample,ifyouareusingPythonasacalculator,youmighttype
>>> miles = 26.2
>>> miles * 1.61
42.182
Thefirstlineassignsavaluetomiles,butithasnovisibleeffect. Thesecondlineisanex-
pression,sotheinterpreterevaluatesitanddisplaystheresult.Itturnsoutthatamarathon
isabout42kilometers.
But if you type the same code into a script and run it, you get no output at all. In script
modeanexpression,allbyitself,hasnovisibleeffect. Pythonevaluatestheexpression,but
itdoesn’tdisplaytheresult. Todisplaytheresult,youneedaprintstatementlikethis:
miles = 26.2
print(miles * 1.61)
This behavior canbe confusing at first. To check yourunderstanding, type the following
statementsinthePythoninterpreterandseewhattheydo:
5
x = 5
x + 1
Nowputthesamestatementsinascriptandrunit. Whatistheoutput? Modifythescript
bytransformingeachexpressionintoaprintstatementandthenrunitagain.
2.5 Order of operations
When an expression contains more than one operator, the order of evaluation depends
on the order of operations. For mathematical operators, Python follows mathematical
convention. TheacronymPEMDASisausefulwaytoremembertherules:

| 12  |     | Chapter2. | Variables,expressionsandstatements |     |
| --- | --- | --------- | ---------------------------------- | --- |
• Parentheses have the highest precedence and can be used to force an expression to
evaluateintheorderyouwant. Sinceexpressionsinparenthesesareevaluatedfirst,
| 2 * (3-1) | (1+1)**(5-2) |       |                              |            |
| --------- | ------------ | ----- | ---------------------------- | ---------- |
|           | is 4, and    | is 8. | You can also use parentheses | to make an |
expression easier to read, as in (minute * 100) / 60, even if it doesn’t change the
result.
|     |     |     | 1 + 2**3 | 2 * |
| --- | --- | --- | -------- | --- |
• Exponentiation has the next highest precedence, so is 9, not 27, and
3**2is18,not36.
• MultiplicationandDivisionhavehigherprecedencethanAdditionandSubtraction.
So2*3-1is5,not4,and6+4/2is8,not5.
• Operatorswiththesameprecedenceareevaluatedfromlefttoright(exceptexponen-
|     |     | degrees / | 2 * pi, |     |
| --- | --- | --------- | ------- | --- |
tiation). So in the expression the division happens first and the
resultismultipliedbypi. Todivideby2π,youcanuseparenthesesorwritedegrees
| / 2 / | pi. |     |     |     |
| ----- | --- | --- | --- | --- |
Idon’tworkveryhardtoremembertheprecedenceofoperators. IfIcan’ttellbylooking
attheexpression,Iuseparenthesestomakeitobvious.
| 2.6 String | operations |     |     |     |
| ---------- | ---------- | --- | --- | --- |
Ingeneral,youcan’tperformmathematicaloperationsonstrings,evenifthestringslook
likenumbers,sothefollowingareillegal:
| 'chinese'-'food' | 'eggs'/'easy' | 'third'*'a | charm' |     |
| ---------------- | ------------- | ---------- | ------ | --- |
Buttherearetwoexceptions,+and*.
The+operatorperformsstringconcatenation,whichmeansitjoinsthestringsbylinking
| themend-to-end. | Forexample: |     |     |     |
| --------------- | ----------- | --- | --- | --- |
| >>> first =     | 'throat'    |     |     |     |
| >>> second      | = 'warbler' |     |     |     |
| >>> first +     | second      |     |     |     |
throatwarbler
The * operator also works on strings; it performs repetition. For example, 'Spam'*3 is
'SpamSpamSpam'.
Ifoneofthevaluesisastring,theotherhastobeaninteger.
Thisuseof+and*makessensebyanalogywithadditionandmultiplication. Justas4*3
isequivalentto4+4+4,weexpect'Spam'*3tobethesameas'Spam'+'Spam'+'Spam',and
itis. Ontheotherhand,thereisasignificantwayinwhichstringconcatenationandrepe-
titionaredifferentfromintegeradditionandmultiplication. Canyouthinkofaproperty
thatadditionhasthatstringconcatenationdoesnot?
2.7 Comments
As programs get bigger and more complicated, they get more difficult to read. Formal
languagesaredense,anditisoftendifficulttolookatapieceofcodeandfigureoutwhat
itisdoing,orwhy.

2.8. Debugging 13
Forthisreason, itisagoodideatoaddnotestoyourprogramstoexplaininnaturallan-
guage what the program is doing. These notes are called comments, and they start with
the#symbol:
# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60
Inthiscase,thecommentappearsonalinebyitself. Youcanalsoputcommentsattheend
ofaline:
percentage = (minute * 100) / 60 # percentage of an hour
Everythingfromthe#totheendofthelineisignored—ithasnoeffectontheexecutionof
theprogram.
Comments are most useful when they document non-obvious features of the code. It is
reasonabletoassumethatthereadercanfigureoutwhatthecodedoes;itismoreusefulto
explainwhy.
Thiscommentisredundantwiththecodeanduseless:
v = 5 # assign 5 to v
Thiscommentcontainsusefulinformationthatisnotinthecode:
v = 5 # velocity in meters/second.
Goodvariablenamescanreducetheneedforcomments, butlongnamescanmakecom-
plexexpressionshardtoread,sothereisatradeoff.
2.8 Debugging
Threekindsoferrorscanoccurinaprogram: syntaxerrors,runtimeerrors,andsemantic
errors. Itisusefultodistinguishbetweentheminordertotrackthemdownmorequickly.
Syntaxerror: “Syntax”referstothestructureofaprogramandtherulesaboutthatstruc-
ture. Forexample,parentheseshavetocomeinmatchingpairs,so(1 + 2)islegal,
but8)isasyntaxerror.
If there is a syntax error anywhere in your program, Python displays an error mes-
sage and quits, and you will not be able to run the program. During the first few
weeks of your programming career, you might spend a lot of time tracking down
syntax errors. As you gain experience, you will make fewer errors and find them
faster.
Runtimeerror: Thesecondtypeoferrorisaruntimeerror,socalledbecausetheerrordoes
notappearuntilaftertheprogramhasstartedrunning. Theseerrorsarealsocalled
exceptions because they usually indicate that something exceptional (and bad) has
happened.
Runtimeerrorsarerareinthesimpleprogramsyouwillseeinthefirstfewchapters,
soitmightbeawhilebeforeyouencounterone.
Semanticerror: The third type of error is “semantic”, which means related to meaning.
If there is a semantic error in your program, it will run without generating error
messages,butitwillnotdotherightthing. Itwilldosomethingelse. Specifically,it
willdowhatyoutoldittodo.
Identifying semantic errors can be tricky because it requires you to work backward
bylookingattheoutputoftheprogramandtryingtofigureoutwhatitisdoing.

14 Chapter2. Variables,expressionsandstatements
2.9 Glossary
variable: Anamethatreferstoavalue.
assignment: Astatementthatassignsavaluetoavariable.
statediagram: Agraphicalrepresentationofasetofvariablesandthevaluestheyreferto.
keyword: Areservedwordthatisusedtoparseaprogram;youcannotusekeywordslike
if,def,andwhileasvariablenames.
operand: Oneofthevaluesonwhichanoperatoroperates.
expression: Acombinationofvariables,operators,andvaluesthatrepresentsasinglere-
sult.
evaluate: Tosimplifyanexpressionbyperformingtheoperationsinordertoyieldasingle
value.
statement: Asectionofcodethatrepresentsacommandoraction. Sofar, thestatements
wehaveseenareassignmentsandprintstatements.
execute: Torunastatementanddowhatitsays.
interactivemode: AwayofusingthePythoninterpreterbytypingcodeattheprompt.
scriptmode: AwayofusingthePythoninterpretertoreadcodefromascriptandrunit.
script: Aprogramstoredinafile.
orderofoperations: Rules governing the order in which expressions involving multiple
operatorsandoperandsareevaluated.
concatenate: Tojointwooperandsend-to-end.
comment: Informationinaprogramthatismeantforotherprogrammers(oranyoneread-
ingthesourcecode)andhasnoeffectontheexecutionoftheprogram.
syntaxerror: An error in a program that makes it impossible to parse (and therefore im-
possibletointerpret).
exception: Anerrorthatisdetectedwhiletheprogramisrunning.
semantics: Themeaningofaprogram.
semanticerror: An error in a program that makes it do something other than what the
programmerintended.
2.10 Exercises
Exercise 2.1. Repeating my advice from the previous chapter, whenever you learn a new feature,
youshouldtryitoutininteractivemodeandmakeerrorsonpurposetoseewhatgoeswrong.
• We’veseenthatn = 42islegal. Whatabout42 = n?

2.10. Exercises 15
• Howaboutx = y = 1?
• In some languages every statement ends with a semi-colon, ;. What happens if you put a
semi-colonattheendofaPythonstatement?
• Whatifyouputaperiodattheendofastatement?
• In math notation you can multiply x and y like this: xy. What happens if you try that in
Python?
Exercise2.2. PracticeusingthePythoninterpreterasacalculator:
1. Thevolumeofaspherewithradiusris 4πr3. Whatisthevolumeofaspherewithradius5?
3
2. Supposethecoverpriceofabookis$24.95,butbookstoresgeta40%discount.Shippingcosts
$3forthefirstcopyand75centsforeachadditionalcopy. Whatisthetotalwholesalecostfor
60copies?
3. IfIleavemyhouseat6:52amandrun1mileataneasypace(8:15permile),then3milesat
tempo(7:12permile)and1mileateasypaceagain,whattimedoIgethomeforbreakfast?

| 16  | Chapter2. | Variables,expressionsandstatements |
| --- | --------- | ---------------------------------- |

Chapter 3
Functions
Inthecontextofprogramming,afunctionisanamedsequenceofstatementsthatperforms
a computation. When you define a function, you specify the name and the sequence of
statements. Later,youcan“call”thefunctionbyname.
3.1 Function calls
Wehavealreadyseenoneexampleofafunctioncall:
>>> type(42)
<class 'int'>
Thenameofthefunctionistype. Theexpressioninparenthesesiscalledtheargumentof
thefunction. Theresult,forthisfunction,isthetypeoftheargument.
Itiscommontosaythatafunction“takes”anargumentand“returns”aresult. Theresult
isalsocalledthereturnvalue.
Pythonprovidesfunctionsthatconvertvaluesfromonetypetoanother. Theintfunction
takesanyvalueandconvertsittoaninteger,ifitcan,orcomplainsotherwise:
>>> int('32')
32
>>> int('Hello')
ValueError: invalid literal for int(): Hello
intcanconvertfloating-pointvaluestointegers,butitdoesn’troundoff; itchopsoffthe
fractionpart:
>>> int(3.99999)
3
>>> int(-2.3)
-2
floatconvertsintegersandstringstofloating-pointnumbers:
>>> float(32)
32.0
>>> float('3.14159')
3.14159

| 18  |     |     |     |     | Chapter3. | Functions |
| --- | --- | --- | --- | --- | --------- | --------- |
Finally,strconvertsitsargumenttoastring:
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
| 3.2 Math | functions |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- |
Python has a math module that provides most of the familiar mathematical functions. A
moduleisafilethatcontainsacollectionofrelatedfunctions.
Before we can use the functions in a module, we have to import it with an import state-
ment:
| >>> import | math |     |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- | --- |
Thisstatementcreatesamoduleobjectnamedmath.Ifyoudisplaythemoduleobject,you
getsomeinformationaboutit:
>>> math
| <module | 'math' (built-in)> |     |     |     |     |     |
| ------- | ------------------ | --- | --- | --- | --- | --- |
The module object contains the functions and variables defined in the module. To access
one of the functions, you have to specify the name of the module and the name of the
function,separatedbyadot(alsoknownasaperiod). Thisformatiscalleddotnotation.
| >>> ratio    | = signal_power      | / noise_power       |     |     |     |     |
| ------------ | ------------------- | ------------------- | --- | --- | --- | --- |
| >>> decibels | = 10                | * math.log10(ratio) |     |     |     |     |
| >>> radians  | = 0.7               |                     |     |     |     |     |
| >>> height   | = math.sin(radians) |                     |     |     |     |     |
Thefirstexampleusesmath.log10tocomputeasignal-to-noiseratioindecibels(assuming
| signal_power |     | noise_power |               |                 |      | log,     |
| ------------ | --- | ----------- | ------------- | --------------- | ---- | -------- |
| that         | and |             | are defined). | The math module | also | provides |
whichcomputeslogarithmsbasee.
The second example finds the sine of radians. The variable name radians is a hint that
| sin |     |     | (cos, | tan, |     |     |
| --- | --- | --- | ----- | ---- | --- | --- |
and the other trigonometric functions etc.) take arguments in radians. To
convertfromdegreestoradians,divideby180andmultiplybyπ:
| >>> degrees | = 45      |         |           |     |     |     |
| ----------- | --------- | ------- | --------- | --- | --- | --- |
| >>> radians | = degrees | / 180.0 | * math.pi |     |     |     |
>>> math.sin(radians)
0.707106781187
Theexpressionmath.pigetsthevariablepifromthemathmodule.
Itsvalueisafloating-
pointapproximationofπ,accuratetoabout15digits.
Ifyouknowtrigonometry,youcancheckthepreviousresultbycomparingittothesquare
rootoftwo,dividedbytwo:
| >>> math.sqrt(2) |     | / 2.0 |     |     |     |     |
| ---------------- | --- | ----- | --- | --- | --- | --- |
0.707106781187

3.3. Composition 19
3.3 Composition
So far, we have looked at the elements of a program—variables, expressions, and
statements—inisolation,withouttalkingabouthowtocombinethem.
One of the most useful features of programming languages is their ability to take small
building blocks and compose them. For example, the argument of a function can be any
kindofexpression,includingarithmeticoperators:
x = math.sin(degrees / 360.0 * 2 * math.pi)
Andevenfunctioncalls:
x = math.exp(math.log(x+1))
Almostanywhereyoucanputavalue, youcanputanarbitraryexpression, withoneex-
ception: the left side of an assignment statement has to be a variable name. Any other
expressionontheleftsideisasyntaxerror(wewillseeexceptionstothisrulelater).
>>> minutes = hours * 60 # right
>>> hours * 60 = minutes # wrong!
SyntaxError: can't assign to operator
3.4 Adding new functions
Sofar,wehaveonlybeenusingthefunctionsthatcomewithPython,butitisalsopossible
toaddnewfunctions. Afunctiondefinitionspecifiesthenameofanewfunctionandthe
sequenceofstatementsthatrunwhenthefunctioniscalled.
Hereisanexample:
def print_lyrics():
print("I'm a lumberjack, and I'm okay.")
print("I sleep all night and I work all day.")
defisakeywordthatindicatesthatthisisafunctiondefinition. Thenameofthefunction
isprint_lyrics. Therulesforfunctionnamesarethesameasforvariablenames: letters,
numbersandunderscorearelegal,butthefirstcharactercan’tbeanumber.Youcan’tusea
keywordasthenameofafunction,andyoushouldavoidhavingavariableandafunction
withthesamename.
The empty parentheses after the name indicate that this function doesn’t take any argu-
ments.
Thefirstlineofthefunctiondefinitioniscalledtheheader;therestiscalledthebody. The
headerhastoendwithacolonandthebodyhastobeindented.Byconvention,indentation
isalwaysfourspaces. Thebodycancontainanynumberofstatements.
Thestringsintheprintstatementsareenclosedindoublequotes.Singlequotesanddouble
quotesdothesamething; mostpeopleusesinglequotesexceptincaseslikethiswherea
singlequote(whichisalsoanapostrophe)appearsinthestring.
All quotation marks (single and double) must be “straight quotes”, usually located next
to Enter on the keyboard. “Curly quotes”, like the ones in this sentence, are not legal in
Python.
Ifyoutypeafunctiondefinitionininteractivemode,theinterpreterprintsdots(...) tolet
youknowthatthedefinitionisn’tcomplete:

| 20      |                 |       |               |       |     |             |        | Chapter3. | Functions |
| ------- | --------------- | ----- | ------------- | ----- | --- | ----------- | ------ | --------- | --------- |
| >>> def | print_lyrics(): |       |               |       |     |             |        |           |           |
| ...     | print("I'm      |       | a lumberjack, |       | and | I'm okay.") |        |           |           |
| ...     | print("I        | sleep | all           | night | and | I work all  | day.") |           |           |
...
Toendthefunction,youhavetoenteranemptyline.
Definingafunctioncreatesafunctionobject,whichhastypefunction:
>>> print(print_lyrics)
| <function | print_lyrics |     | at  | 0xb7e99e9c> |     |     |     |     |     |
| --------- | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- |
>>> type(print_lyrics)
<class 'function'>
Thesyntaxforcallingthenewfunctionisthesameasforbuilt-infunctions:
>>> print_lyrics()
| I'm a lumberjack, |     | and       | I'm | okay.    |      |     |     |     |     |
| ----------------- | --- | --------- | --- | -------- | ---- | --- | --- | --- | --- |
| I sleep           | all | night and | I   | work all | day. |     |     |     |     |
Onceyouhavedefinedafunction,youcanuseitinsideanotherfunction. Forexample,to
repeatthepreviousrefrain,wecouldwriteafunctioncalledrepeat_lyrics:
def repeat_lyrics():
print_lyrics()
print_lyrics()
Andthencallrepeat_lyrics:
>>> repeat_lyrics()
| I'm a lumberjack, |     | and       | I'm | okay.    |      |     |     |     |     |
| ----------------- | --- | --------- | --- | -------- | ---- | --- | --- | --- | --- |
| I sleep           | all | night and | I   | work all | day. |     |     |     |     |
| I'm a lumberjack, |     | and       | I'm | okay.    |      |     |     |     |     |
| I sleep           | all | night and | I   | work all | day. |     |     |     |     |
Butthat’snotreallyhowthesonggoes.
| 3.5 Definitions |     |     | and | uses |     |     |     |     |     |
| --------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Pulling together the code fragments from the previous section, the whole program looks
likethis:
def print_lyrics():
| print("I'm |     | a lumberjack, |           | and | I'm    | okay.")    |     |     |     |
| ---------- | --- | ------------- | --------- | --- | ------ | ---------- | --- | --- | --- |
| print("I   |     | sleep         | all night | and | I work | all day.") |     |     |     |
def repeat_lyrics():
print_lyrics()
print_lyrics()
repeat_lyrics()
print_lyricsandrepeat_lyrics.
| Thisprogramcontainstwofunctiondefinitions: |     |     |     |     |     |     |     |     | Func- |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
tion definitions get executed just like other statements, but the effect is to create function
objects. Thestatementsinsidethefunctiondonotrununtilthefunctioniscalled,andthe
functiondefinitiongeneratesnooutput.

3.6. Flowofexecution 21
Asyoumightexpect,youhavetocreateafunctionbeforeyoucanrunit. Inotherwords,
thefunctiondefinitionhastorunbeforethefunctiongetscalled.
As an exercise, move the last line of this program to the top, so the function call appears
beforethedefinitions. Runtheprogramandseewhaterrormessageyouget.
Nowmovethefunctioncallbacktothebottomandmovethedefinitionofprint_lyrics
afterthedefinitionofrepeat_lyrics. Whathappenswhenyourunthisprogram?
3.6 Flow of execution
Toensurethatafunctionisdefinedbeforeitsfirstuse, youhavetoknowtheorderstate-
mentsrunin,whichiscalledtheflowofexecution.
Executionalwaysbeginsatthefirststatementoftheprogram. Statementsarerunoneata
time,inorderfromtoptobottom.
Functiondefinitionsdonotaltertheflowofexecutionoftheprogram,butrememberthat
statementsinsidethefunctiondon’trununtilthefunctioniscalled.
Afunctioncallislikeadetourintheflowofexecution. Insteadofgoingtothenextstate-
ment,theflowjumpstothebodyofthefunction,runsthestatementsthere,andthencomes
backtopickupwhereitleftoff.
Thatsoundssimpleenough,untilyourememberthatonefunctioncancallanother. While
in the middle of one function, the program might have to run the statements in another
function. Then, while runningthat newfunction, theprogram mighthave to runyet an-
otherfunction!
Fortunately, Python is good at keeping track of where it is, so each time a function com-
pletes,theprogrampicksupwhereitleftoffinthefunctionthatcalledit. Whenitgetsto
theendoftheprogram,itterminates.
Insummary,whenyoureadaprogram,youdon’talwayswanttoreadfromtoptobottom.
Sometimesitmakesmoresenseifyoufollowtheflowofexecution.
3.7 Parameters and arguments
Some of the functions we have seen require arguments. For example, when you call
math.sin you pass a number as an argument. Some functions take more than one ar-
gument: math.powtakestwo,thebaseandtheexponent.
Inside the function, the arguments are assigned to variables called parameters. Here is a
definitionforafunctionthattakesanargument:
def print_twice(bruce):
print(bruce)
print(bruce)
This function assigns the argument to a parameter named bruce. When the function is
called,itprintsthevalueoftheparameter(whateveritis)twice.
Thisfunctionworkswithanyvaluethatcanbeprinted.

| 22  |     |     |     | Chapter3. | Functions |
| --- | --- | --- | --- | --------- | --------- |
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(42)
42
42
>>> print_twice(math.pi)
3.14159265359
3.14159265359
Thesamerulesofcompositionthatapplytobuilt-infunctionsalsoapplytoprogrammer-
definedfunctions,sowecanuseanykindofexpressionasanargumentforprint_twice:
| >>> print_twice('Spam |           | '*4) |     |     |     |
| --------------------- | --------- | ---- | --- | --- | --- |
| Spam Spam             | Spam Spam |      |     |     |     |
| Spam Spam             | Spam Spam |      |     |     |     |
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
Theargumentisevaluatedbeforethefunctioniscalled,sointheexamplestheexpressions
'Spam '*4andmath.cos(math.pi)areonlyevaluatedonce.
Youcanalsouseavariableasanargument:
| >>> michael | = 'Eric, | the half a bee.' |     |     |     |
| ----------- | -------- | ---------------- | --- | --- | --- |
>>> print_twice(michael)
| Eric, the | half a | bee. |     |     |     |
| --------- | ------ | ---- | --- | --- | --- |
| Eric, the | half a | bee. |     |     |     |
(michael)
The name of the variable we pass as an argument has nothing to do with the
nameoftheparameter(bruce). Itdoesn’tmatterwhatthevaluewascalledbackhome(in
thecaller);hereinprint_twice,wecalleverybodybruce.
| 3.8 Variables |     | and parameters | are local |     |     |
| ------------- | --- | -------------- | --------- | --- | --- |
When you create a variable inside a function, it is local, which means that it only exists
| insidethefunction.   |           | Forexample: |     |     |     |
| -------------------- | --------- | ----------- | --- | --- | --- |
| def cat_twice(part1, |           | part2):     |     |     |     |
| cat                  | = part1 + | part2       |     |     |     |
print_twice(cat)
Thisfunctiontakestwoarguments,concatenatesthem,andprintstheresulttwice. Hereis
anexamplethatusesit:
| >>> line1            | = 'Bing   | tiddle ' |     |     |     |
| -------------------- | --------- | -------- | --- | --- | --- |
| >>> line2            | = 'tiddle | bang.'   |     |     |     |
| >>> cat_twice(line1, |           | line2)   |     |     |     |
| Bing tiddle          | tiddle    | bang.    |     |     |     |
| Bing tiddle          | tiddle    | bang.    |     |     |     |
Whencat_twiceterminates,thevariablecatisdestroyed.
Ifwetrytoprintit,wegetan
exception:

| 3.9. Stackdiagrams |     |     |       |                |     | 23  |
| ------------------ | --- | --- | ----- | -------------- | --- | --- |
|                    |     |     | line1 | ’Bing tiddle ’ |     |     |
__main__
|     |     |             | line2 | ’tiddle bang.’             |     |     |
| --- | --- | ----------- | ----- | -------------------------- | --- | --- |
|     |     |             | part1 | ’Bing tiddle ’             |     |     |
|     |     | cat_twice   | part2 | ’tiddle bang.’             |     |     |
|     |     |             | cat   | ’Bing tiddle tiddle bang.’ |     |     |
|     |     | print_twice | bruce | ’Bing tiddle tiddle bang.’ |     |     |
Figure3.1: Stackdiagram.
>>> print(cat)
| NameError: | name | 'cat' is not | defined |     |     |     |
| ---------- | ---- | ------------ | ------- | --- | --- | --- |
print_twice,
Parameters are also local. For example, outside there is no such thing as
bruce.
| 3.9 Stack | diagrams |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- |
Tokeeptrackofwhichvariablescanbeusedwhere,itissometimesusefultodrawastack
diagram. Like state diagrams, stack diagrams show the value of each variable, but they
alsoshowthefunctioneachvariablebelongsto.
Each function is represented by a frame. A frame is a box with the name of a function
besideitandtheparametersandvariablesofthefunctioninsideit. Thestackdiagramfor
thepreviousexampleisshowninFigure3.1.
The frames are arranged in a stack that indicates which function called which, and so
|        |               | print_twice |            | cat_twice, | cat_twice |            |
| ------ | ------------- | ----------- | ---------- | ---------- | --------- | ---------- |
| on. In | this example, |             | was called | by         | and       | was called |
by__main__, whichisaspecialnameforthetopmostframe. Whenyoucreateavariable
outsideofanyfunction,itbelongsto__main__.
So,part1hasthe
Eachparameterreferstothesamevalueasitscorrespondingargument.
samevalueasline1,part2hasthesamevalueasline2,andbrucehasthesamevalueas
cat.
Ifanerroroccursduringafunctioncall,Pythonprintsthenameofthefunction,thename
ofthefunctionthatcalledit,andthenameofthefunctionthatcalledthat,allthewayback
to__main__.
Forexample,ifyoutrytoaccesscatfromwithinprint_twice,yougetaNameError:
| Traceback        | (innermost | last):   |              |     |     |     |
| ---------------- | ---------- | -------- | ------------ | --- | --- | --- |
| File             | "test.py", | line 13, | in __main__  |     |     |     |
| cat_twice(line1, |            | line2)   |              |     |     |     |
| File             | "test.py", | line 5,  | in cat_twice |     |     |     |
print_twice(cat)
| File | "test.py", | line 9, | in print_twice |     |     |     |
| ---- | ---------- | ------- | -------------- | --- | --- | --- |
print(cat)
| NameError: | name | 'cat' is not | defined |     |     |     |
| ---------- | ---- | ------------ | ------- | --- | --- | --- |

24 Chapter3. Functions
Thislistoffunctionsiscalledatraceback. Ittellsyouwhatprogramfiletheerroroccurred
in,andwhatline,andwhatfunctionswereexecutingatthetime. Italsoshowsthelineof
codethatcausedtheerror.
The order of the functions in the traceback is the same as the order of the frames in the
stackdiagram. Thefunctionthatiscurrentlyrunningisatthebottom.
3.10 Fruitful functions and void functions
Someofthefunctionswehaveused,suchasthemathfunctions,returnresults;forlackof
abettername, Icallthemfruitfulfunctions. Otherfunctions, likeprint_twice, perform
anactionbutdon’treturnavalue. Theyarecalledvoidfunctions.
Whenyoucallafruitfulfunction,youalmostalwayswanttodosomethingwiththeresult;
forexample,youmightassignittoavariableoruseitaspartofanexpression:
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
Whenyoucallafunctionininteractivemode,Pythondisplaystheresult:
>>> math.sqrt(5)
2.2360679774997898
Butinascript,ifyoucallafruitfulfunctionallbyitself,thereturnvalueislostforever!
math.sqrt(5)
Thisscriptcomputesthesquarerootof5,butsinceitdoesn’tstoreordisplaytheresult,it
isnotveryuseful.
Voidfunctionsmightdisplaysomethingonthescreenorhavesomeothereffect,butthey
don’t have a return value. If you assign the result to a variable, you get a special value
calledNone.
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
ThevalueNoneisnotthesameasthestring'None'. Itisaspecialvaluethathasitsown
type:
>>> type(None)
<class 'NoneType'>
Thefunctionswehavewrittensofarareallvoid. Wewillstartwritingfruitfulfunctionsin
afewchapters.
3.11 Why functions?
Itmaynotbeclearwhyitisworththetroubletodivideaprogramintofunctions. There
areseveralreasons:

3.12. Debugging 25
• Creating a new function gives you an opportunity to name a group of statements,
whichmakesyourprogrameasiertoreadanddebug.
• Functionscanmakea programsmallerbyeliminatingrepetitivecode. Later, ifyou
makeachange,youonlyhavetomakeitinoneplace.
• Dividingalongprogramintofunctionsallowsyoutodebugthepartsoneatatime
andthenassemblethemintoaworkingwhole.
• Well-designed functions are often useful for many programs. Once you write and
debugone,youcanreuseit.
3.12 Debugging
One of the most important skills you will acquire is debugging. Although it can be frus-
trating,debuggingisoneofthemostintellectuallyrich,challenging,andinterestingparts
ofprogramming.
In some ways debugging is like detective work. You are confronted with clues and you
havetoinfertheprocessesandeventsthatledtotheresultsyousee.
Debuggingisalsolikeanexperimentalscience.Onceyouhaveanideaaboutwhatisgoing
wrong, youmodifyyourprogramandtryagain. Ifyourhypothesiswascorrect,youcan
predicttheresultofthemodification,andyoutakeastepclosertoaworkingprogram. If
your hypothesis was wrong, you have to come up with a new one. As Sherlock Holmes
pointedout,“Whenyouhaveeliminatedtheimpossible,whateverremains,howeverim-
probable,mustbethetruth.” (A.ConanDoyle,TheSignofFour)
Forsomepeople,programminganddebuggingarethesamething. Thatis,programming
istheprocessofgraduallydebuggingaprogramuntilitdoeswhatyouwant. Theideais
thatyoushouldstartwithaworkingprogramandmakesmallmodifications, debugging
themasyougo.
For example, Linux is an operating system that contains millions of lines of code, but it
started out as a simple program Linus Torvalds used to explore the Intel 80386 chip. Ac-
cording to Larry Greenfield, “One of Linus’s earlier projects was a program that would
switchbetweenprintingAAAAandBBBB.ThislaterevolvedtoLinux.” (TheLinuxUsers’
GuideBetaVersion1).
3.13 Glossary
function: A named sequence of statements that performs some useful operation. Func-
tionsmayormaynottakeargumentsandmayormaynotproducearesult.
functiondefinition: Astatementthatcreatesanewfunction,specifyingitsname,param-
eters,andthestatementsitcontains.
functionobject: A value created by a function definition. The name of the function is a
variablethatreferstoafunctionobject.
header: Thefirstlineofafunctiondefinition.

26 Chapter3. Functions
body: Thesequenceofstatementsinsideafunctiondefinition.
parameter: Anameusedinsideafunctiontorefertothevaluepassedasanargument.
functioncall: Astatementthatrunsafunction. Itconsistsofthefunctionnamefollowed
byanargumentlistinparentheses.
argument: A value provided to a function when the function is called. This value is as-
signedtothecorrespondingparameterinthefunction.
localvariable: A variable defined inside a function. A local variable can only be used
insideitsfunction.
returnvalue: Theresultofafunction. Ifafunctioncallisusedasanexpression,thereturn
valueisthevalueoftheexpression.
fruitfulfunction: Afunctionthatreturnsavalue.
voidfunction: AfunctionthatalwaysreturnsNone.
None: Aspecialvaluereturnedbyvoidfunctions.
module: Afilethatcontainsacollectionofrelatedfunctionsandotherdefinitions.
importstatement: Astatementthatreadsamodulefileandcreatesamoduleobject.
moduleobject: Avaluecreatedbyanimportstatementthatprovidesaccesstothevalues
definedinamodule.
dotnotation: Thesyntaxforcallingafunctioninanothermodulebyspecifyingthemod-
ulenamefollowedbyadot(period)andthefunctionname.
composition: Usinganexpressionaspartofalargerexpression,orastatementaspartof
alargerstatement.
flowofexecution: Theorderstatementsrunin.
stackdiagram: Agraphicalrepresentationofastackoffunctions,theirvariables,andthe
valuestheyreferto.
frame: Aboxinastackdiagramthatrepresentsafunctioncall. Itcontainsthelocalvari-
ablesandparametersofthefunction.
traceback: Alistofthefunctionsthatareexecuting,printedwhenanexceptionoccurs.
3.14 Exercises
Exercise3.1. Writeafunctionnamedright_justifythattakesastringnamedsasaparameter
andprintsthestringwithenoughleadingspacessothatthelastletterofthestringisincolumn70
ofthedisplay.
>>> right_justify('monty')
monty
Hint:Usestringconcatenationandrepetition. Also,Pythonprovidesabuilt-infunctioncalledlen
thatreturnsthelengthofastring,sothevalueoflen('monty')is5.

3.14. Exercises 27
Exercise3.2. Afunctionobjectisavalueyoucanassigntoavariableorpassasanargument. For
example,do_twiceisafunctionthattakesafunctionobjectasanargumentandcallsittwice:
def do_twice(f):
f()
f()
Here’sanexamplethatusesdo_twicetocallafunctionnamedprint_spamtwice.
def print_spam():
print('spam')
do_twice(print_spam)
1. Typethisexampleintoascriptandtestit.
Modifydo_twicesothatittakestwoarguments,afunctionobjectandavalue,andcallsthe
2.
functiontwice,passingthevalueasanargument.
3. Copythedefinitionofprint_twicefromearlierinthischaptertoyourscript.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
argument.
Defineanewfunctioncalleddo_fourthattakesafunctionobjectandavalueandcallsthe
5.
functionfourtimes,passingthevalueasaparameter. Thereshouldbeonlytwostatementsin
thebodyofthisfunction,notfour.
Solution: https://thinkpython.com/code/do_four.py.
Exercise3.3. Note: Thisexerciseshouldbedoneusingonlythestatementsandotherfeatureswe
havelearnedsofar.
1. Writeafunctionthatdrawsagridlikethefollowing:
| + - - - | - + - - - | - + |
| ------- | --------- | --- |
| |       | |         | |   |
| |       | |         | |   |
| |       | |         | |   |
| |       | |         | |   |
| + - - - | - + - - - | - + |
| |       | |         | |   |
| |       | |         | |   |
| |       | |         | |   |
| |       | |         | |   |
| + - - - | - + - - - | - + |
Hint: to print more than one value on a line, you can print a comma-separated sequence of
values:
| print('+', | '-') |     |
| ---------- | ---- | --- |
By default, print advances to the next line, but you can override that behavior and put a
spaceattheend,likethis:
| print('+', | end=' | ')  |
| ---------- | ----- | --- |
print('-')

28 Chapter3. Functions
The output of these statements is '+ -' on the same line. The output from the next print
statementwouldbeginonthenextline.
2. Writeafunctionthatdrawsasimilargridwithfourrowsandfourcolumns.
Solution: https://thinkpython.com/code/grid.py. Credit: This exercise is based on an
exerciseinOualline,PracticalCProgramming,ThirdEdition,O’ReillyMedia,1997.

| Chapter | 4      |           |        |
| ------- | ------ | --------- | ------ |
| Case    | study: | interface | design |
Thischapterpresentsacasestudythatdemonstratesaprocessfordesigningfunctionsthat
worktogether.
Itintroducestheturtlemodule,whichallowsyoutocreateimagesusingturtlegraphics.
TheturtlemoduleisincludedinmostPythoninstallations,butifyouarerunningPython
usingPythonAnywhere,youwon’tbeabletoruntheturtleexamples(atleastyoucouldn’t
whenIwrotethis).
If you have already installed Python on your computer, you should be able to run the
http:
examples. Otherwise, now is a good time to install. I have posted instructions at
//tinyurl.com/thinkpython2e.
Code examples from this chapter are available from https://thinkpython.com/code/
polygon.py.
| 4.1 The | turtle module |     |     |
| ------- | ------------- | --- | --- |
Tocheckwhetheryouhavetheturtlemodule,openthePythoninterpreterandtype
| >>> import | turtle            |     |     |
| ---------- | ----------------- | --- | --- |
| >>> bob    | = turtle.Turtle() |     |     |
Whenyourunthiscode,itshouldcreateanewwindowwithsmallarrowthatrepresents
| theturtle. | Closethewindow. |     |     |
| ---------- | --------------- | --- | --- |
Createafilenamedmypolygon.pyandtypeinthefollowingcode:
import turtle
bob = turtle.Turtle()
print(bob)
turtle.mainloop()
Theturtlemodule(withalowercase’t’)providesafunctioncalledTurtle(withanup-
percase’T’)thatcreatesaTurtleobject,whichweassigntoavariablenamedbob. Printing
bobdisplayssomethinglike:
| <turtle.Turtle | object | at 0xb7bfbf4c> |     |
| -------------- | ------ | -------------- | --- |

30 Chapter4. Casestudy: interfacedesign
ThismeansthatbobreferstoanobjectwithtypeTurtleasdefinedinmoduleturtle.
mainloop tells the window to wait for the user to do something, although in this case
there’snotmuchfortheusertodoexceptclosethewindow.
OnceyoucreateaTurtle,youcancallamethodtomoveitaroundthewindow. Amethod
issimilartoafunction,butitusesslightlydifferentsyntax. Forexample,tomovetheturtle
forward:
bob.fd(100)
Themethod,fd,isassociatedwiththeturtleobjectwe’recallingbob. Callingamethodis
likemakingarequest: youareaskingbobtomoveforward.
Theargumentoffdisadistanceinpixels,sotheactualsizedependsonyourdisplay.
OthermethodsyoucancallonaTurtlearebktomovebackward, ltforleftturn, andrt
rightturn. Theargumentforltandrtisanangleindegrees.
Also,eachTurtleisholdingapen,whichiseitherdownorup;ifthepenisdown,theTurtle
leavesatrailwhenitmoves. Themethodspuandpdstandfor“penup”and“pendown”.
Todrawarightangle,addtheselinestotheprogram(aftercreatingbobandbeforecalling
mainloop):
bob.fd(100)
bob.lt(90)
bob.fd(100)
When you run this program, you should see bob move east and then north, leaving two
linesegmentsbehind.
Nowmodifytheprogramtodrawasquare. Don’tgoonuntilyou’vegotitworking!
4.2 Simple repetition
Chancesareyouwrotesomethinglikethis:
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
We can do the same thing more concisely with a for statement. Add this example to
mypolygon.pyandrunitagain:
for i in range(4):
print('Hello!')
Youshouldseesomethinglikethis:

4.3. Exercises 31
Hello!
Hello!
Hello!
Hello!
This is the simplest use of the for statement; we will see more later. But that should be
enoughtoletyourewriteyoursquare-drawingprogram. Don’tgoonuntilyoudo.
Hereisaforstatementthatdrawsasquare:
for i in range(4):
bob.fd(100)
bob.lt(90)
Thesyntaxofaforstatementissimilartoafunctiondefinition. Ithasaheaderthatends
withacolonandanindentedbody. Thebodycancontainanynumberofstatements.
Aforstatementisalsocalledaloopbecausetheflowofexecutionrunsthroughthebody
andthenloopsbacktothetop. Inthiscase,itrunsthebodyfourtimes.
Thisversionisactuallyalittledifferentfromtheprevioussquare-drawingcodebecauseit
makes another turn after drawing the last side of the square. The extra turn takes more
time,butitsimplifiesthecodeifwedothesamethingeverytimethroughtheloop. This
version also has the effect of leaving the turtle back in the starting position, facing in the
startingdirection.
4.3 Exercises
Thefollowingisaseriesofexercisesusingtheturtlemodule. Theyaremeanttobefun,
buttheyhaveapoint,too. Whileyouareworkingonthem,thinkaboutwhatthepointis.
Thefollowingsectionshavesolutionstotheexercises,sodon’tlookuntilyouhavefinished
(oratleasttried).
1. Writeafunctioncalledsquarethattakesaparameternamedt, whichisaturtle. It
shouldusetheturtletodrawasquare.
Write a function call that passes bob as an argument to square, and then run the
programagain.
2. Addanotherparameter,namedlength,tosquare. Modifythebodysolengthofthe
sidesislength,andthenmodifythefunctioncalltoprovideasecondargument.Run
theprogramagain. Testyourprogramwitharangeofvaluesforlength.
3. Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterioranglesofann-sidedregularpolygonare360/ndegrees.
4. Writeafunctioncalledcirclethattakesaturtle,t,andradius,r,asparametersand
thatdrawsanapproximatecirclebycallingpolygonwithanappropriatelengthand
numberofsides. Testyourfunctionwitharangeofvaluesofr.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
5. Makeamoregeneralversionofcirclecalledarcthattakesanadditionalparameter
angle,whichdetermineswhatfractionofacircletodraw.angleisinunitsofdegrees,
sowhenangle=360,arcshoulddrawacompletecircle.

| 32  |     |     | Chapter4. | Casestudy: | interfacedesign |     |
| --- | --- | --- | --------- | ---------- | --------------- | --- |
4.4 Encapsulation
Thefirstexerciseasksyoutoputyoursquare-drawingcodeintoafunctiondefinitionand
| thencallthefunction,passingtheturtleasaparameter. |     |     |     | Hereisasolution: |     |     |
| ------------------------------------------------- | --- | --- | --- | ---------------- | --- | --- |
def square(t):
| for | i in range(4): |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
t.fd(100)
t.lt(90)
square(bob)
The innermost statements, fd and lt are indented twice to show that they are inside the
forloop,whichisinsidethefunctiondefinition. Thenextline,square(bob),isflushwith
theleftmargin,whichindicatestheendofboththeforloopandthefunctiondefinition.
|     | t   |     | bob, | t.lt(90) |     |     |
| --- | --- | --- | ---- | -------- | --- | --- |
Inside the function, refers to the same turtle so has the same effect as
| bob.lt(90). |               |         |                    | bob?     | t           |        |
| ----------- | ------------- | ------- | ------------------ | -------- | ----------- | ------ |
|             | In that case, | why not | call the parameter | The idea | is that can | be any |
turtle,notjustbob,soyoucouldcreateasecondturtleandpassitasanargumenttosquare:
| alice = | turtle.Turtle() |     |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- | --- |
square(alice)
Wrappingapieceofcodeupinafunctioniscalledencapsulation. Oneofthebenefitsof
encapsulationisthatitattachesanametothecode,whichservesasakindofdocumenta-
tion. Anotheradvantageisthatifyoure-usethecode,itismoreconcisetocallafunction
twicethantocopyandpastethebody!
4.5 Generalization
| Thenextstepistoaddalengthparametertosquare. |                |     |     | Hereisasolution: |     |     |
| ------------------------------------------- | -------------- | --- | --- | ---------------- | --- | --- |
| def square(t,                               | length):       |     |     |                  |     |     |
| for                                         | i in range(4): |     |     |                  |     |     |
t.fd(length)
t.lt(90)
| square(bob, | 100) |     |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- | --- |
Adding a parameter to a function is called generalization because it makes the function
moregeneral: inthepreviousversion,thesquareisalwaysthesamesize;inthisversionit
canbeanysize.
Insteadofdrawingsquares,polygondrawsregular
Thenextstepisalsoageneralization.
| polygonswithanynumberofsides. |                |     | Hereisasolution: |     |     |     |
| ----------------------------- | -------------- | --- | ---------------- | --- | --- | --- |
| def polygon(t,                | n, length):    |     |                  |     |     |     |
| angle                         | = 360 / n      |     |                  |     |     |     |
| for                           | i in range(n): |     |                  |     |     |     |
t.fd(length)
t.lt(angle)
| polygon(bob, | 7, 70) |     |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- |

| 4.6. Interfacedesign |     |     |     |     |     | 33  |
| -------------------- | --- | --- | --- | --- | --- | --- |
Thisexampledrawsa7-sidedpolygonwithsidelength70.
angle
If you are using Python 2, the value of might be off because of integer division. A
simple solution is to compute angle = 360.0 / n. Because the numerator is a floating-
pointnumber,theresultisfloatingpoint.
Whenafunctionhasmorethanafewnumericarguments,itiseasytoforgetwhattheyare,
orwhatordertheyshouldbein. Inthatcaseitisoftenagoodideatoincludethenamesof
theparametersintheargumentlist:
| polygon(bob, | n=7, | length=70) |     |     |     |     |
| ------------ | ---- | ---------- | --- | --- | --- | --- |
Thesearecalledkeywordargumentsbecausetheyincludetheparameternamesas“key-
words”(nottobeconfusedwithPythonkeywordslikewhileanddef).
Thissyntaxmakestheprogrammorereadable. Itisalsoareminderabouthowarguments
andparameterswork: whenyoucallafunction,theargumentsareassignedtotheparam-
eters.
| 4.6 Interface |     | design |     |     |     |     |
| ------------- | --- | ------ | --- | --- | --- | --- |
Thenextstepistowritecircle,whichtakesaradius,r,asaparameter.
Hereisasimple
solutionthatusespolygontodrawa50-sidedpolygon:
import math
| def circle(t, | r):             |               |     |     |     |     |
| ------------- | --------------- | ------------- | --- | --- | --- | --- |
| circumference |                 | = 2 * math.pi | * r |     |     |     |
| n = 50        |                 |               |     |     |     |     |
| length        | = circumference |               | / n |     |     |     |
| polygon(t,    | n,              | length)       |     |     |     |     |
Thefirstlinecomputesthecircumferenceofacirclewithradiusrusingtheformula2πr.
|          | math.pi, |         | math.     |                | import     |     |
| -------- | -------- | ------- | --------- | -------------- | ---------- | --- |
| Since we | use      | we have | to import | By convention, | statements | are |
usuallyatthebeginningofthescript.
nisthenumberoflinesegmentsinourapproximationofacircle, solengthisthelength
ofeachsegment. Thus,polygondrawsa50-sidedpolygonthatapproximatesacirclewith
radiusr.
Onelimitationofthissolutionisthatnisaconstant,whichmeansthatforverybigcircles,
the line segments are too long, and for small circles, we waste time drawing very small
n
segments. One solution would be to generalize the function by taking as a parameter.
Thiswouldgivetheuser(whoevercallscircle)morecontrol,buttheinterfacewouldbe
lessclean.
Theinterfaceofafunctionisasummaryofhowitisused: whataretheparameters? What
doesthefunctiondo? Andwhatisthereturnvalue? Aninterfaceis“clean”ifitallowsthe
callertodowhattheywantwithoutdealingwithunnecessarydetails.
Inthisexample, rbelongsintheinterfacebecauseitspecifiesthecircletobedrawn. nis
lessappropriatebecauseitpertainstothedetailsofhowthecircleshouldberendered.
Ratherthanclutteruptheinterface,itisbettertochooseanappropriatevalueofndepend-
ingoncircumference:

| 34                    |               |               | Chapter4. | Casestudy: | interfacedesign |
| --------------------- | ------------- | ------------- | --------- | ---------- | --------------- |
| def circle(t,         | r):           |               |           |            |                 |
| circumference         | = 2           | * math.pi * r |           |            |                 |
| n = int(circumference |               | / 3) + 3      |           |            |                 |
| length =              | circumference | / n           |           |            |                 |
| polygon(t,            | n, length)    |               |           |            |                 |
circumference/3,
Now the number of segments is an integer near so the length of each
segment is approximately 3, which is small enough that the circles look good, but big
enoughtobeefficient,andacceptableforanysizecircle.
Adding3tonguaranteesthatthepolygonhasatleast3sides.
4.7 Refactoring
WhenIwrotecircle,Iwasabletore-usepolygonbecauseamany-sidedpolygonisagood
Butarcisnotascooperative;wecan’tusepolygonorcircleto
approximationofacircle.
drawanarc.
|     |     | polygon |     |     | arc. |
| --- | --- | ------- | --- | --- | ---- |
One alternative is to start with a copy of and transform it into The result
mightlooklikethis:
| def arc(t, r,      | angle):       |             |       |     |     |
| ------------------ | ------------- | ----------- | ----- | --- | --- |
| arc_length         | = 2 * math.pi | * r * angle | / 360 |     |     |
| n = int(arc_length |               | / 3) + 1    |       |     |     |
| step_length        | = arc_length  | / n         |       |     |     |
| step_angle         | = angle       | / n         |       |     |     |
| for i in           | range(n):     |             |       |     |     |
t.fd(step_length)
t.lt(step_angle)
The second half of this function looks like polygon, but we can’t re-use polygon without
Wecouldgeneralizepolygontotakeanangleasathirdargument,
changingtheinterface.
but then polygon would no longer be an appropriate name! Instead, let’s call the more
generalfunctionpolyline:
| def polyline(t, | n, length, | angle): |     |     |     |
| --------------- | ---------- | ------- | --- | --- | --- |
| for i in        | range(n):  |         |     |     |     |
t.fd(length)
t.lt(angle)
Nowwecanrewritepolygonandarctousepolyline:
| def polygon(t,     | n, length):     |             |       |     |     |
| ------------------ | --------------- | ----------- | ----- | --- | --- |
| angle =            | 360.0 / n       |             |       |     |     |
| polyline(t,        | n, length,      | angle)      |       |     |     |
| def arc(t, r,      | angle):         |             |       |     |     |
| arc_length         | = 2 * math.pi   | * r * angle | / 360 |     |     |
| n = int(arc_length |                 | / 3) + 1    |       |     |     |
| step_length        | = arc_length    | / n         |       |     |     |
| step_angle         | = float(angle)  | / n         |       |     |     |
| polyline(t,        | n, step_length, | step_angle) |       |     |     |
Finally,wecanrewritecircletousearc:

4.8. Adevelopmentplan 35
| def circle(t, | r):     |     |     |
| ------------- | ------- | --- | --- |
| arc(t,        | r, 360) |     |     |
This process—rearranging a program to improve interfaces and facilitate code re-use—is
Inthiscase,wenoticedthattherewassimilarcodeinarcandpolygon,
calledrefactoring.
sowe“factoreditout”intopolyline.
wemighthavewrittenpolylinefirstandavoidedrefactoring,
Ifwehadplannedahead,
butoftenyoudon’tknowenoughatthebeginningofaprojecttodesignalltheinterfaces.
Onceyoustartcoding,youunderstandtheproblembetter. Sometimesrefactoringisasign
thatyouhavelearnedsomething.
| 4.8 A development |     | plan |     |
| ----------------- | --- | ---- | --- |
Adevelopmentplanisaprocessforwritingprograms. Theprocessweusedinthiscase
| studyis“encapsulationandgeneralization”. |     | Thestepsofthisprocessare: |     |
| ---------------------------------------- | --- | ------------------------- | --- |
1. Startbywritingasmallprogramwithnofunctiondefinitions.
2. Once you get the program working, identify a coherent piece of it, encapsulate the
pieceinafunctionandgiveitaname.
3. Generalizethefunctionbyaddingappropriateparameters.
4. Repeatsteps1–3untilyouhaveasetofworkingfunctions. Copyandpasteworking
codetoavoidretyping(andre-debugging).
5. Look for opportunities to improve the program by refactoring. For example, if you
havesimilarcodeinseveralplaces,considerfactoringitintoanappropriatelygeneral
function.
This process has some drawbacks—we will see alternatives later—but it can be useful if
you don’t know ahead of time how to divide the program into functions. This approach
letsyoudesignasyougoalong.
4.9 docstring
A docstring is a string at the beginning of a function that explains the interface (“doc” is
| shortfor“documentation”). |                  | Hereisanexample: |              |
| ------------------------- | ---------------- | ---------------- | ------------ |
| def polyline(t,           | n, length,       | angle):          |              |
| """Draws                  | n line segments  | with the given   | length and   |
| angle (in                 | degrees) between | them. t          | is a turtle. |
"""
| for i in | range(n): |     |     |
| -------- | --------- | --- | --- |
t.fd(length)
t.lt(angle)
By convention, all docstrings are triple-quoted strings, also known as multiline strings
becausethetriplequotesallowthestringtospanmorethanoneline.

36 Chapter4. Casestudy: interfacedesign
Itisterse, butitcontainstheessentialinformationsomeonewouldneedtousethisfunc-
tion. Itexplainsconciselywhatthefunctiondoes(withoutgettingintothedetailsofhow
itdoesit). Itexplainswhateffecteachparameterhasonthebehaviorofthefunctionand
whattypeeachparametershouldbe(ifitisnotobvious).
Writing this kind of documentation is an important part of interface design. A well-
designed interface should be simple to explain; if you have a hard time explaining one
ofyourfunctions,maybetheinterfacecouldbeimproved.
4.10 Debugging
Aninterfaceislikeacontractbetweenafunctionandacaller. Thecalleragreestoprovide
certainparametersandthefunctionagreestodocertainwork.
Forexample,polylinerequiresfourarguments:thastobeaTurtle;nhastobeaninteger;
lengthshouldbeapositivenumber;andanglehastobeanumber,whichisunderstood
tobeindegrees.
Theserequirementsarecalledpreconditionsbecausetheyaresupposedtobetruebefore
the function starts executing. Conversely, conditions at the end of the function are post-
conditions. Postconditions include the intended effect of the function (like drawing line
segments)andanysideeffects(likemovingtheTurtleormakingotherchanges).
Preconditions are the responsibility of the caller. If the caller violates a (properly docu-
mented!) preconditionandthefunctiondoesn’tworkcorrectly,thebugisinthecaller,not
thefunction.
Ifthepreconditionsaresatisfiedandthepostconditionsarenot,thebugisinthefunction.
Ifyourpre-andpostconditionsareclear,theycanhelpwithdebugging.
4.11 Glossary
method: Afunctionthatisassociatedwithanobjectandcalledusingdotnotation.
loop: Apartofaprogramthatcanrunrepeatedly.
encapsulation: Theprocessoftransformingasequenceofstatementsintoafunctiondefi-
nition.
generalization: Theprocessofreplacingsomethingunnecessarilyspecific(likeanumber)
withsomethingappropriatelygeneral(likeavariableorparameter).
keywordargument: An argument that includes the name of the parameter as a “key-
word”.
interface: Adescriptionofhowtouseafunction,includingthenameanddescriptionsof
theargumentsandreturnvalue.
refactoring: Theprocessofmodifyingaworkingprogramtoimprovefunctioninterfaces
andotherqualitiesofthecode.
developmentplan: Aprocessforwritingprograms.

4.12. Exercises 37
Figure4.1: Turtleflowers.
Figure4.2: Turtlepies.
docstring: Astringthatappearsatthetopofafunctiondefinitiontodocumentthefunc-
tion’sinterface.
precondition: Arequirementthatshouldbesatisfiedbythecallerbeforeafunctionstarts.
postcondition: Arequirementthatshouldbesatisfiedbythefunctionbeforeitends.
4.12 Exercises
Exercise 4.1. Download the code in this chapter from https://thinkpython.com/code/
polygon.py.
1. Draw a stack diagram that shows the state of the program while executing circle(bob,
radius). Youcandothearithmeticbyhandoraddprintstatementstothecode.
2. TheversionofarcinSection4.7isnotveryaccuratebecausethelinearapproximationofthe
circleisalwaysoutsidethetruecircle. Asaresult,theTurtleendsupafewpixelsawayfrom
thecorrectdestination. Mysolutionshowsawaytoreducetheeffectofthiserror. Readthe
codeandseeifitmakessensetoyou. Ifyoudrawadiagram,youmightseehowitworks.
Exercise4.2. WriteanappropriatelygeneralsetoffunctionsthatcandrawflowersasinFigure4.1.
Solution: https://thinkpython.com/code/flower.py, also requires https:
//thinkpython.com/code/polygon.py.
Exercise4.3. WriteanappropriatelygeneralsetoffunctionsthatcandrawshapesasinFigure4.2.
Solution: https://thinkpython.com/code/pie.py.
Exercise 4.4. The letters of the alphabet can be constructed from a moderate number of basic ele-
ments, like vertical and horizontal lines and a few curves. Design an alphabet that can be drawn
withaminimalnumberofbasicelementsandthenwritefunctionsthatdrawtheletters.
You should write one function for each letter, with names draw_a, draw_b, etc., and put your
functions in a file named letters.py. You can download a “turtle typewriter” from https:
//thinkpython.com/code/typewriter.py tohelpyoutestyourcode.

38 Chapter4. Casestudy: interfacedesign
Youcangetasolutionfromhttps://thinkpython.com/code/letters.py; italsorequires
https://thinkpython.com/code/polygon.py.
Exercise 4.5. Read about spirals at http://en.wikipedia.org/wiki/Spiral; then write
a program that draws an Archimedian spiral (or one of the other kinds). Solution: https://
thinkpython.com/code/spiral.py.

| Chapter      | 5   |     |           |
| ------------ | --- | --- | --------- |
| Conditionals |     | and | recursion |
Themaintopicofthischapteristheifstatement,whichexecutesdifferentcodedepending
onthestateoftheprogram. ButfirstIwanttointroducetwonewoperators: floordivision
andmodulus.
| 5.1 Floor | division | and modulus |     |
| --------- | -------- | ----------- | --- |
Thefloordivisionoperator,//,dividestwonumbersandroundsdowntoaninteger. For
example, supposetheruntimeofamovieis105minutes. Youmightwanttoknowhow
| longthatisinhours. |       | Conventionaldivisionreturnsafloating-pointnumber: |     |
| ------------------ | ----- | ------------------------------------------------- | --- |
| >>> minutes        | = 105 |                                                   |     |
| >>> minutes        | / 60  |                                                   |     |
1.75
Butwedon’tnormallywritehourswithdecimalpoints. Floordivisionreturnstheinteger
numberofhours,roundingdown:
| >>> minutes | = 105     |       |     |
| ----------- | --------- | ----- | --- |
| >>> hours   | = minutes | // 60 |     |
>>> hours
1
Togettheremainder,youcouldsubtractoffonehourinminutes:
| >>> remainder | = minutes | - hours | * 60 |
| ------------- | --------- | ------- | ---- |
>>> remainder
45
Analternativeistousethemodulusoperator,%,whichdividestwonumbersandreturns
theremainder.
| >>> remainder | = minutes | % 60 |     |
| ------------- | --------- | ---- | --- |
>>> remainder
45
Themodulusoperatorismoreusefulthanitseems. Forexample,youcancheckwhether
| onenumberisdivisiblebyanother—ifx |     |     | % yiszero,thenxisdivisiblebyy. |
| --------------------------------- | --- | --- | ------------------------------ |

| 40  |     |     | Chapter5. | Conditionalsandrecursion |     |
| --- | --- | --- | --------- | ------------------------ | --- |
x % 10
Also, you can extract the right-most digit or digits from a number. For example,
yieldstheright-mostdigitofx(inbase10). Similarlyx % 100yieldsthelasttwodigits.
If you are using Python 2, division works differently. The division operator, /, performs
floordivisionifbothoperandsareintegers,andfloating-pointdivisionifeitheroperandis
afloat.
| 5.2 Boolean | expressions |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- |
Abooleanexpressionisanexpressionthatiseithertrueorfalse. Thefollowingexamples
use the operator ==, which compares two operands and produces True if they are equal
andFalseotherwise:
| >>> 5 == 5 |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
True
| >>> 5 == 6 |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
False
TrueandFalsearespecialvaluesthatbelongtothetypebool;theyarenotstrings:
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
The==operatorisoneoftherelationaloperators;theothersare:
| x !=  | y   | # x is | not equal to | y             |     |
| ----- | --- | ------ | ------------ | ------------- | --- |
| x > y |     | # x is | greater than | y             |     |
| x < y |     | # x is | less than y  |               |     |
| x >=  | y   | # x is | greater than | or equal to y |     |
| x <=  | y   | # x is | less than or | equal to y    |     |
Althoughtheseoperationsareprobablyfamiliartoyou,thePythonsymbolsaredifferent
fromthemathematicalsymbols.Acommonerroristouseasingleequalsign(=)insteadof
adoubleequalsign(==). Rememberthat=isanassignmentoperatorand==isarelational
Thereisnosuchthingas=<or=>.
operator.
| 5.3 Logical     | operators          |      |          |                     |          |
| --------------- | ------------------ | ---- | -------- | ------------------- | -------- |
|                 | logical operators: | and, | or, not. |                     |          |
| There are three |                    |      | and The  | semantics (meaning) | of these |
|                 |                    |      |          | x > 0 and x         | < 10     |
operators is similar to their meaning in English. For example, is true
onlyifxisgreaterthan0andlessthan10.
n%2 == 0 or n%3 == 0istrueifeitherorbothoftheconditionsistrue,thatis,ifthenumber
isdivisibleby2or3.
Finally, the not operator negates a boolean expression, so not (x > y) is true if x > y is
false,thatis,ifxislessthanorequaltoy.
Strictlyspeaking,theoperandsofthelogicaloperatorsshouldbebooleanexpressions,but
| Pythonisnotverystrict. | AnynonzeronumberisinterpretedasTrue: |     |     |     |     |
| ---------------------- | ------------------------------------ | --- | --- | --- | --- |

5.4. Conditionalexecution 41
>>> 42 and True
True
This flexibility can be useful, but there are some subtleties to it that might be confusing.
Youmightwanttoavoidit(unlessyouknowwhatyouaredoing).
| 5.4 Conditional | execution |     |     |
| --------------- | --------- | --- | --- |
Inordertowriteusefulprograms, wealmostalwaysneedtheabilitytocheckconditions
andchangethebehavioroftheprogramaccordingly. Conditionalstatementsgiveusthis
Thesimplestformistheifstatement:
ability.
if x > 0:
| print('x is | positive') |     |     |
| ----------- | ---------- | --- | --- |
Thebooleanexpressionafterifiscalledthecondition. Ifitistrue,theindentedstatement
runs. Ifnot,nothinghappens.
if statements have the same structure as function definitions: a header followed by an
| indentedbody. Statementslikethisarecalledcompoundstatements. |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- |
Thereisnolimitonthenumberofstatementsthatcanappearinthebody,buttherehasto
be at least one. Occasionally, it is useful to have a body with no statements (usually as a
placekeeperforcodeyouhaven’twrittenyet).Inthatcase,youcanusethepassstatement,
whichdoesnothing.
if x < 0:
| pass            | # TODO: need | to handle | negative values! |
| --------------- | ------------ | --------- | ---------------- |
| 5.5 Alternative | execution    |           |                  |
Asecondformoftheifstatementis“alternativeexecution”,inwhichtherearetwopossi-
bilitiesandtheconditiondetermineswhichoneruns. Thesyntaxlookslikethis:
| if x % 2 == 0: |        |     |     |
| -------------- | ------ | --- | --- |
| print('x is    | even') |     |     |
else:
| print('x is | odd') |     |     |
| ----------- | ----- | --- | --- |
Iftheremainderwhenxisdividedby2is0,thenweknowthatxiseven,andtheprogram
displays an appropriate message. If the condition is false, the second set of statements
runs. Sincetheconditionmustbetrueorfalse,exactlyoneofthealternativeswillrun. The
alternativesarecalledbranches,becausetheyarebranchesintheflowofexecution.
| 5.6 Chained | conditionals |     |     |
| ----------- | ------------ | --- | --- |
Sometimes there are more than two possibilities and we need more than two branches.
Onewaytoexpressacomputationlikethatisachainedconditional:

| 42  |     |     |     |     | Chapter5. | Conditionalsandrecursion |
| --- | --- | --- | --- | --- | --------- | ------------------------ |
if x < y:
| print('x |        | is less than | y')  |     |     |     |
| -------- | ------ | ------------ | ---- | --- | --- | --- |
| elif     | x > y: |              |      |     |     |     |
| print('x |        | is greater   | than | y') |     |     |
else:
| print('x |     | and y are | equal') |     |     |     |
| -------- | --- | --------- | ------- | --- | --- | --- |
elifisanabbreviationof“elseif”.Again,exactlyonebranchwillrun.Thereisnolimiton
thenumberofelifstatements. Ifthereisanelseclause,ithastobeattheend,butthere
doesn’thavetobeone.
| if choice | ==  | 'a': |     |     |     |     |
| --------- | --- | ---- | --- | --- | --- | --- |
draw_a()
| elif | choice == | 'b': |     |     |     |     |
| ---- | --------- | ---- | --- | --- | --- | --- |
draw_b()
| elif | choice == | 'c': |     |     |     |     |
| ---- | --------- | ---- | --- | --- | --- | --- |
draw_c()
Eachconditionischeckedinorder. Ifthefirstisfalse,thenextischecked,andsoon. Ifone
ofthemistrue,thecorrespondingbranchrunsandthestatementends. Evenifmorethan
oneconditionistrue,onlythefirsttruebranchruns.
| 5.7 | Nested | conditionals |     |     |     |     |
| --- | ------ | ------------ | --- | --- | --- | --- |
Oneconditionalcanalsobenestedwithinanother. Wecouldhavewrittentheexamplein
theprevioussectionlikethis:
| if x     | == y: |           |         |     |     |     |
| -------- | ----- | --------- | ------- | --- | --- | --- |
| print('x |       | and y are | equal') |     |     |     |
else:
| if  | x < y:   |         |      |     |     |     |
| --- | -------- | ------- | ---- | --- | --- | --- |
|     | print('x | is less | than | y') |     |     |
else:
|     | print('x | is greater |     | than y') |     |     |
| --- | -------- | ---------- | --- | -------- | --- | --- |
Theouterconditionalcontainstwobranches. Thefirstbranchcontainsasimplestatement.
The second branch contains another if statement, which has two branches of its own.
Thosetwobranchesarebothsimplestatements,althoughtheycouldhavebeenconditional
statementsaswell.
Although the indentation of the statements makes the structure apparent, nested condi-
tionals become difficult to read very quickly. It is a good idea to avoid them when you
can.
Logical operators often provide a way to simplify nested conditional statements. For ex-
ample,wecanrewritethefollowingcodeusingasingleconditional:
if 0 < x:
| if  | x < 10:  |               |     |              |           |     |
| --- | -------- | ------------- | --- | ------------ | --------- | --- |
|     | print('x | is a positive |     | single-digit | number.') |     |
Theprintstatementrunsonlyifwemakeitpastbothconditionals,sowecangetthesame
effectwiththeandoperator:
| if 0     | < x and | x < 10:       |              |     |           |     |
| -------- | ------- | ------------- | ------------ | --- | --------- | --- |
| print('x |         | is a positive | single-digit |     | number.') |     |

| 5.8. Recursion |     |     |     |     |     |     |     |     |     | 43  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Forthiskindofcondition,Pythonprovidesamoreconciseoption:
if 0 < x < 10:
| print('x |     | is a | positive | single-digit |     | number.') |     |     |     |     |
| -------- | --- | ---- | -------- | ------------ | --- | --------- | --- | --- | --- | --- |
5.8 Recursion
Itislegalforonefunctiontocallanother;itisalsolegalforafunctiontocallitself. Itmay
not be obvious why that is a good thing, but it turns out to be one of the most magical
| thingsaprogramcando. |     |     | Forexample,lookatthefollowingfunction: |     |     |     |     |     |     |     |
| -------------------- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
def countdown(n):
| if  | n <= 0: |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
print('Blastoff!')
else:
print(n)
countdown(n-1)
Ifnis0ornegative,itoutputstheword,“Blastoff!” Otherwise,itoutputsnandthencalls
afunctionnamedcountdown—itself—passingn-1asanargument.
Whathappensifwecallthisfunctionlikethis?
>>> countdown(3)
The execution of countdown begins with n=3, and since n is greater than 0, it outputs the
value3,andthencallsitself...
|     |           |     | countdown |        |      | n=2, |           | n   |              |       |
| --- | --------- | --- | --------- | ------ | ---- | ---- | --------- | --- | ------------ | ----- |
| The | execution | of  |           | begins | with |      | and since | is  | greater than | 0, it |
outputsthevalue2,andthencallsitself...
|     | The | execution | of  | countdown | begins | with | n=1, and | since | n is greater |     |
| --- | --- | --------- | --- | --------- | ------ | ---- | -------- | ----- | ------------ | --- |
than0,itoutputsthevalue1,andthencallsitself...
|     |     | The execution                                |     | of countdown |     | begins with | n=0, | and since | n is |     |
| --- | --- | -------------------------------------------- | --- | ------------ | --- | ----------- | ---- | --------- | ---- | --- |
|     |     | notgreaterthan0,itoutputstheword,“Blastoff!” |     |              |     |             |      | andthen   |      |     |
returns.
Thecountdownthatgotn=1returns.
Thecountdownthatgotn=2returns.
Thecountdownthatgotn=3returns.
| Andthenyou’rebackin__main__. |     |     |     |     | So,thetotaloutputlookslikethis: |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
3
2
1
Blastoff!
Afunctionthatcallsitselfisrecursive;theprocessofexecutingitiscalledrecursion.
Asanotherexample,wecanwriteafunctionthatprintsastringntimes.
| def print_n(s, |         | n): |     |     |     |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| if             | n <= 0: |     |     |     |     |     |     |     |     |     |
return
print(s)
| print_n(s, |     | n-1) |     |     |     |     |     |     |     |     |
| ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |

| 44  |     |     | Chapter5. | Conditionalsandrecursion |
| --- | --- | --- | --------- | ------------------------ |
__main__
|     |     | countdown                | n 3 |     |
| --- | --- | ------------------------ | --- | --- |
|     |     | countdown                | n 2 |     |
|     |     | countdown                | n 1 |     |
|     |     | countdown                | n 0 |     |
|     |     | Figure5.1: Stackdiagram. |     |     |
If n <= 0 the return statement exits the function. The flow of execution immediately re-
turnstothecaller,andtheremaininglinesofthefunctiondon’trun.
Therestofthefunctionissimilartocountdown: itdisplayssandthencallsitselftodisplay
sn−1additionaltimes. Sothenumberoflinesofoutputis1 + (n - 1),whichaddsup
ton.
for
For simple examples like this, it is probably easier to use a loop. But we will see
exampleslaterthatarehardtowritewithaforloopandeasytowritewithrecursion,soit
isgoodtostartearly.
| 5.9 Stack | diagrams | for recursive | functions |     |
| --------- | -------- | ------------- | --------- | --- |
InSection3.9,weusedastackdiagramtorepresentthestateofaprogramduringafunction
call. Thesamekindofdiagramcanhelpinterpretarecursivefunction.
Every time a function gets called, Python creates a frame to contain the function’s local
variablesandparameters. Forarecursivefunction,theremightbemorethanoneframeon
thestackatthesametime.
| Figure5.1showsastackdiagramforcountdowncalledwithn |     |     |     | = 3. |
| -------------------------------------------------- | --- | --- | --- | ---- |
__main__.
As usual, the top of the stack is the frame for It is empty because we did not
createanyvariablesin__main__orpassanyargumentstoit.
The four countdown frames have different values for the parameter n. The bottom of the
stack,wheren=0,iscalledthebasecase.
Itdoesnotmakearecursivecall,sothereareno
moreframes.
Asanexercise,drawastackdiagramforprint_ncalledwiths = 'Hello'andn=2.
Then
writeafunctioncalleddo_nthattakesafunctionobjectandanumber,n,asarguments,and
thatcallsthegivenfunctionntimes.
| 5.10 Infinite | recursion |     |     |     |
| ------------- | --------- | --- | --- | --- |
Ifarecursionneverreachesabasecase,itgoesonmakingrecursivecallsforever,andthe
program never terminates. This is known as infinite recursion, and it is generally not a
| goodidea. Hereisaminimalprogramwithaninfiniterecursion: |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- |

5.11. Keyboardinput 45
def recurse():
recurse()
Inmostprogrammingenvironments,aprogramwithinfiniterecursiondoesnotreallyrun
forever. Pythonreportsanerrormessagewhenthemaximumrecursiondepthisreached:
| File | "<stdin>", | line | 2,  | in recurse |     |     |
| ---- | ---------- | ---- | --- | ---------- | --- | --- |
| File | "<stdin>", | line | 2,  | in recurse |     |     |
| File | "<stdin>", | line | 2,  | in recurse |     |     |
.
.
.
| File          | "<stdin>", | line | 2,        | in recurse |                |     |
| ------------- | ---------- | ---- | --------- | ---------- | -------------- | --- |
| RuntimeError: | Maximum    |      | recursion |            | depth exceeded |     |
Thistracebackisalittlebiggerthantheonewesawinthepreviouschapter.Whentheerror
occurs,thereare1000recurseframesonthestack!
If you encounter an infinite recursion by accident, review your function to confirm that
thereisabasecasethatdoesnotmakearecursivecall. Andifthereisabasecase, check
whetheryouareguaranteedtoreachit.
| 5.11 | Keyboard |     | input |     |     |     |
| ---- | -------- | --- | ----- | --- | --- | --- |
Theprogramswehavewrittensofaracceptnoinputfromtheuser. Theyjustdothesame
thingeverytime.
Pythonprovidesabuilt-infunctioncalledinputthatstopstheprogramandwaitsforthe
usertotypesomething. WhentheuserpressesReturnorEnter,theprogramresumesand
input returns what the user typed as a string. In Python 2, the same function is called
raw_input.
| >>> text | = input()   |     |      |     |     |     |
| -------- | ----------- | --- | ---- | --- | --- | --- |
| What are | you waiting |     | for? |     |     |     |
>>> text
| 'What are | you waiting |     | for?' |     |     |     |
| --------- | ----------- | --- | ----- | --- | --- | --- |
Beforegettinginputfromtheuser,itisagoodideatoprintaprompttellingtheuserwhat
totype. inputcantakeapromptasanargument:
| >>> name  | = input('What...is |       |          | your | name?\n') |     |
| --------- | ------------------ | ----- | -------- | ---- | --------- | --- |
| What...is | your               | name? |          |      |           |     |
| Arthur,   | King of            | the   | Britons! |      |           |     |
>>> name
| 'Arthur, | King of | the | Britons!' |     |     |     |
| -------- | ------- | --- | --------- | --- | --- | --- |
Thesequence\nattheendofthepromptrepresentsanewline,whichisaspecialcharacter
thatcausesalinebreak. That’swhytheuser’sinputappearsbelowtheprompt.
Ifyouexpecttheusertotypeaninteger,youcantrytoconvertthereturnvaluetoint:
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
| >>> speed | = input(prompt) |     |          |     |               |          |
| --------- | --------------- | --- | -------- | --- | ------------- | -------- |
| What...is | the airspeed    |     | velocity |     | of an unladen | swallow? |
42
>>> int(speed)
42

| 46  |     |     |     |     |     | Chapter5. | Conditionalsandrecursion |
| --- | --- | --- | --- | --- | --- | --------- | ------------------------ |
Butiftheusertypessomethingotherthanastringofdigits,yougetanerror:
| >>> speed | = input(prompt) |          |          |     |               |          |          |
| --------- | --------------- | -------- | -------- | --- | ------------- | -------- | -------- |
| What...is | the             | airspeed | velocity |     | of an unladen |          | swallow? |
| What do   | you mean,       | an       | African  | or  | a European    | swallow? |          |
>>> int(speed)
| ValueError: | invalid |     | literal | for | int() with | base | 10  |
| ----------- | ------- | --- | ------- | --- | ---------- | ---- | --- |
Wewillseehowtohandlethiskindoferrorlater.
5.12 Debugging
Whenasyntaxorruntimeerroroccurs,theerrormessagecontainsalotofinformation,but
| itcanbeoverwhelming. |     |     | Themostusefulpartsareusually: |     |     |     |     |
| -------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |
• Whatkindoferroritwas,and
• Whereitoccurred.
Syntaxerrorsareusuallyeasytofind,butthereareafewgotchas. Whitespaceerrorscan
betrickybecausespacesandtabsareinvisibleandweareusedtoignoringthem.
| >>> x = | 5          |      |     |     |     |     |     |
| ------- | ---------- | ---- | --- | --- | --- | --- | --- |
| >>> y   | = 6        |      |     |     |     |     |     |
| File    | "<stdin>", | line | 1   |     |     |     |     |
| y =     | 6          |      |     |     |     |     |     |
^
| IndentationError: |     | unexpected |     | indent |     |     |     |
| ----------------- | --- | ---------- | --- | ------ | --- | --- | --- |
Inthisexample,theproblemisthatthesecondlineisindentedbyonespace. Buttheerror
y,
message points to which is misleading. In general, error messages indicate where the
problemwasdiscovered,buttheactualerrormightbeearlierinthecode,sometimesona
previousline.
The same is true of runtime errors. Suppose you are trying to compute a signal-to-noise
|     |     |     |     |     | =   | (P  | ).  |
| --- | --- | --- | --- | --- | --- | --- | --- |
ratio in decibels. The formula is SNR db 10log signal /P noise In Python, you might
10
writesomethinglikethis:
import math
| signal_power | =            | 9                   |                |     |     |     |     |
| ------------ | ------------ | ------------------- | -------------- | --- | --- | --- | --- |
| noise_power  | =            | 10                  |                |     |     |     |     |
| ratio =      | signal_power |                     | // noise_power |     |     |     |     |
| decibels     | = 10         | * math.log10(ratio) |                |     |     |     |     |
print(decibels)
Whenyourunthisprogram,yougetanexception:
| Traceback   | (most     | recent | call              | last): |     |     |     |
| ----------- | --------- | ------ | ----------------- | ------ | --- | --- | --- |
| File        | "snr.py", | line   | 5,                | in ?   |     |     |     |
| decibels    | =         | 10 *   | math.log10(ratio) |        |     |     |     |
| ValueError: | math      | domain | error             |        |     |     |     |
The error message indicates line 5, but there is nothing wrong with that line. To find the
ratio,
real error, it might be useful to print the value of which turns out to be 0. The
problemisinline4,whichusesfloordivisioninsteadoffloating-pointdivision.
Youshouldtakethetimetoreaderrormessagescarefully,butdon’tassumethateverything
theysayiscorrect.

5.13. Glossary 47
5.13 Glossary
floordivision: Anoperator,denoted//,thatdividestwonumbersandroundsdown(to-
wardnegativeinfinity)toaninteger.
modulusoperator: An operator, denoted with a percent sign (%), that works on integers
andreturnstheremainderwhenonenumberisdividedbyanother.
booleanexpression: AnexpressionwhosevalueiseitherTrueorFalse.
relationaloperator: Oneoftheoperatorsthatcomparesitsoperands: ==,!=,>,<,>=,and
<=.
logicaloperator: One of the operators that combines boolean expressions: and, or, and
not.
conditionalstatement: Astatementthatcontrolstheflowofexecutiondependingonsome
condition.
condition: The boolean expression in a conditional statement that determines which
branchruns.
compoundstatement: Astatementthatconsistsofaheaderandabody. Theheaderends
withacolon(:). Thebodyisindentedrelativetotheheader.
branch: Oneofthealternativesequencesofstatementsinaconditionalstatement.
chainedconditional: Aconditionalstatementwithaseriesofalternativebranches.
nestedconditional: Aconditionalstatementthatappearsinoneofthebranchesofanother
conditionalstatement.
returnstatement: Astatementthatcausesafunctiontoendimmediatelyandreturntothe
caller.
recursion: Theprocessofcallingthefunctionthatiscurrentlyexecuting.
basecase: Aconditionalbranchinarecursivefunctionthatdoesnotmakearecursivecall.
infiniterecursion: Arecursionthatdoesn’thaveabasecase,orneverreachesit. Eventu-
ally,aninfiniterecursioncausesaruntimeerror.
5.14 Exercises
Exercise 5.1. The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
UNIXsystems,theepochis1January1970.
>>> import time
>>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours, minutes, and
seconds,plusthenumberofdayssincetheepoch.

48 Chapter5. Conditionalsandrecursion
Exercise5.2. Fermat’sLastTheoremsaysthattherearenopositiveintegersa,b,andcsuchthat
an+bn = cn
foranyvaluesofngreaterthan2.
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
checkstoseeifFermat’stheoremholds. Ifnisgreaterthan2and
an+bn = cn
theprogramshouldprint,“Holysmokes,Fermatwaswrong!”Otherwisetheprogramshould
print,“No,thatdoesn’twork.”
2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers,andusescheck_fermattocheckwhethertheyviolateFermat’stheorem.
Exercise5.3. Ifyouaregiventhreesticks,youmayormaynotbeabletoarrangetheminatriangle.
Forexample,ifoneofthesticksis12incheslongandtheothertwoareoneinchlong,youwillnot
beabletogettheshortstickstomeetinthemiddle. Foranythreelengths,thereisasimpletestto
seeifitispossibletoformatriangle:
Ifanyofthethreelengthsisgreaterthanthesumoftheothertwo,thenyoucannot
formatriangle. Otherwise,youcan. (Ifthesumoftwolengthsequalsthethird,they
formwhatiscalleda“degenerate”triangle.)
1. Writeafunctionnamedis_trianglethattakesthreeintegersasarguments,andthatprints
either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
withthegivenlengths.
2. Writeafunctionthatpromptstheusertoinputthreesticklengths,convertsthemtointegers,
andusesis_triangletocheckwhetherstickswiththegivenlengthscanformatriangle.
Exercise5.4. Whatistheoutputofthefollowingprogram? Drawastackdiagramthatshowsthe
stateoftheprogramwhenitprintstheresult.
def recurse(n, s):
if n == 0:
print(s)
else:
recurse(n-1, n+s)
recurse(3, 0)
1. Whatwouldhappenifyoucalledthisfunctionlikethis: recurse(-1, 0)?
2. Writeadocstringthatexplainseverythingsomeonewouldneedtoknowinordertousethis
function(andnothingelse).
Thefollowingexercisesusetheturtlemodule,describedinChapter4:
Exercise5.5. Readthefollowingfunctionandseeifyoucanfigureoutwhatitdoes(seetheexam-
plesinChapter4). Thenrunitandseeifyougotitright.

5.14. Exercises 49
Figure5.2: AKochcurve.
def draw(t, length, n):
if n == 0:
return
angle = 50
t.fd(length*n)
t.lt(angle)
draw(t, length, n-1)
t.rt(2*angle)
draw(t, length, n-1)
t.lt(angle)
t.bk(length*n)
Exercise 5.6. The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
curvewithlengthx,allyouhavetodois
1. DrawaKochcurvewithlengthx/3.
2. Turnleft60degrees.
3. DrawaKochcurvewithlengthx/3.
4. Turnright120degrees.
5. DrawaKochcurvewithlengthx/3.
6. Turnleft60degrees.
7. DrawaKochcurvewithlengthx/3.
Theexceptionisifxislessthan3: inthatcase,youcanjustdrawastraightlinewithlengthx.
1. Writeafunctioncalledkochthattakesaturtleandalengthasparameters,andthatusesthe
turtletodrawaKochcurvewiththegivenlength.
2. Write a function called snowflake that draws three Koch curves to make the outline of a
snowflake.
Solution: https://thinkpython.com/code/koch.py.
3. The Koch curve can be generalized in several ways. See http://en.wikipedia.org/
wiki/Koch_snowflake forexamplesandimplementyourfavorite.

| 50  | Chapter5. | Conditionalsandrecursion |
| --- | --------- | ------------------------ |

Chapter 6
Fruitful functions
Many of the Python functions we have used, such as the math functions, produce return
values. But the functions we’ve written are all void: they have an effect, like printing a
valueormovingaturtle,buttheydon’thaveareturnvalue. Inthischapteryouwilllearn
towritefruitfulfunctions.
6.1 Return values
Callingthefunctiongeneratesareturnvalue,whichweusuallyassigntoavariableoruse
aspartofanexpression.
e = math.exp(1.0)
height = radius * math.sin(radians)
The functions we have written so far are void. Speaking casually, they have no return
value;moreprecisely,theirreturnvalueisNone.
Inthischapter,weare(finally)goingtowritefruitfulfunctions. Thefirstexampleisarea,
whichreturnstheareaofacirclewiththegivenradius:
def area(radius):
a = math.pi * radius**2
return a
Wehaveseenthereturnstatementbefore,butinafruitfulfunctionthereturnstatement
includes an expression. This statement means: “Return immediately from this function
and use the following expression as a return value.” The expression can be arbitrarily
complicated,sowecouldhavewrittenthisfunctionmoreconcisely:
def area(radius):
return math.pi * radius**2
Ontheotherhand,temporaryvariableslikeacanmakedebuggingeasier.
Sometimes it is useful to have multiple return statements, one in each branch of a condi-
tional:

| 52  |     |     |     | Chapter6. | Fruitfulfunctions |
| --- | --- | --- | --- | --------- | ----------------- |
def absolute_value(x):
| if x | < 0: |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- |
return -x
else:
return x
Sincethesereturnstatementsareinanalternativeconditional,onlyoneruns.
Assoonasareturnstatementruns,thefunctionterminateswithoutexecutinganysubse-
Codethatappearsafterareturnstatement,oranyotherplacetheflow
quentstatements.
ofexecutioncanneverreach,iscalleddeadcode.
Inafruitfulfunction,itisagoodideatoensurethateverypossiblepaththroughthepro-
gramhitsareturnstatement.
Forexample:
def absolute_value(x):
| if x | < 0: |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- |
return -x
| if x | > 0: |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- |
return x
x
This function is incorrect because if happens to be 0, neither condition is true, and the
functionendswithouthittingareturnstatement. Iftheflowofexecutiongetstotheend
ofafunction,thereturnvalueisNone,whichisnottheabsolutevalueof0.
>>> print(absolute_value(0))
None
Bytheway,Pythonprovidesabuilt-infunctioncalledabsthatcomputesabsolutevalues.
Asanexercise,writeacomparefunctionthattakestwovalues,xandy,andreturns1ifx
| > y,0ifx        | == y,and-1ifx | < y.        |     |     |     |
| --------------- | ------------- | ----------- | --- | --- | --- |
| 6.2 Incremental |               | development |     |     |     |
Asyouwritelargerfunctions,youmightfindyourselfspendingmoretimedebugging.
To deal with increasingly complex programs, you might want to try a process called in-
crementaldevelopment. Thegoalofincrementaldevelopmentistoavoidlongdebugging
sessionsbyaddingandtestingonlyasmallamountofcodeatatime.
As an example, suppose you want to find the distance between two points, given by the
coordinates(x ,y )and(x ,y ). BythePythagoreantheorem,thedistanceis:
|     | 1 1 | 2 2 |     |     |     |
| --- | --- | --- | --- | --- | --- |
(cid:113)
|     |     | distance= | (x −x )2+(y | −y )2 |     |
| --- | --- | --------- | ----------- | ----- | --- |
|     |     |           | 2 1         | 2 1   |     |
ThefirststepistoconsiderwhatadistancefunctionshouldlooklikeinPython.
Inother
words,whataretheinputs(parameters)andwhatistheoutput(returnvalue)?
Inthiscase, theinputsaretwopoints, whichyoucanrepresentusingfournumbers. The
returnvalueisthedistancerepresentedbyafloating-pointvalue.
Immediatelyyoucanwriteanoutlineofthefunction:
| def distance(x1, | y1, | x2, y2): |     |     |     |
| ---------------- | --- | -------- | --- | --- | --- |
| return           | 0.0 |          |     |     |     |

6.2. Incrementaldevelopment 53
Obviously, this version doesn’t compute distances; it always returns zero. But it is syn-
tactically correct, and it runs, which means that you can test it before you make it more
complicated.
Totestthenewfunction,callitwithsamplearguments:
>>> distance(1, 2, 4, 6)
0.0
Ichosethesevaluessothatthehorizontaldistanceis3andtheverticaldistanceis4; that
way,theresultis5,thehypotenuseofa3-4-5righttriangle. Whentestingafunction,itis
usefultoknowtherightanswer.
Atthispointwehaveconfirmedthatthefunctionissyntacticallycorrect,andwecanstart
adding code to the body. A reasonable next step is to find the differences x −x and
2 1
y −y . Thenextversionstoresthosevaluesintemporaryvariablesandprintsthem.
2 1
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
print('dx is', dx)
print('dy is', dy)
return 0.0
Ifthefunctionisworking,itshoulddisplaydx is 3anddy is 4. Ifso,weknowthatthe
functionisgettingtherightargumentsandperformingthefirstcomputationcorrectly. If
not,thereareonlyafewlinestocheck.
Nextwecomputethesumofsquaresofdxanddy:
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
print('dsquared is: ', dsquared)
return 0.0
Again, you would run the program at this stage and check the output (which should be
25). Finally,youcanusemath.sqrttocomputeandreturntheresult:
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
result = math.sqrt(dsquared)
return result
If that works correctly, you are done. Otherwise, you might want to print the value of
resultbeforethereturnstatement.
The final version of the function doesn’t display anything when it runs; it only returns
a value. The print statements we wrote are useful for debugging, but once you get the
functionworking,youshouldremovethem. Codelikethatiscalledscaffoldingbecauseit
ishelpfulforbuildingtheprogrambutisnotpartofthefinalproduct.
Whenyoustartout,youshouldaddonlyalineortwoofcodeatatime. Asyougainmore
experience, you might find yourself writing and debugging bigger chunks. Either way,
incrementaldevelopmentcansaveyoualotofdebuggingtime.
Thekeyaspectsoftheprocessare:

54 Chapter6. Fruitfulfunctions
1. Startwithaworkingprogramandmakesmallincrementalchanges. Atanypoint,if
thereisanerror,youshouldhaveagoodideawhereitis.
2. Usevariablestoholdintermediatevaluessoyoucandisplayandcheckthem.
3. Oncetheprogramisworking,youmightwanttoremovesomeofthescaffoldingor
consolidate multiple statements into compound expressions, but only if it does not
maketheprogramdifficulttoread.
As an exercise, use incremental development to write a function called hypotenuse that
returnsthelengthofthehypotenuseofarighttrianglegiventhelengthsoftheothertwo
legsasarguments. Recordeachstageofthedevelopmentprocessasyougo.
6.3 Composition
Asyoushouldexpectbynow,youcancallonefunctionfromwithinanother. Asanexam-
ple,we’llwriteafunctionthattakestwopoints,thecenterofthecircleandapointonthe
perimeter,andcomputestheareaofthecircle.
Assumethatthecenterpointisstoredinthevariablesxcandyc,andtheperimeterpointis
inxpandyp. Thefirststepistofindtheradiusofthecircle,whichisthedistancebetween
thetwopoints. Wejustwroteafunction,distance,thatdoesthat:
radius = distance(xc, yc, xp, yp)
Thenextstepistofindtheareaofacirclewiththatradius;wejustwrotethat,too:
result = area(radius)
Encapsulatingthesestepsinafunction,weget:
def circle_area(xc, yc, xp, yp):
radius = distance(xc, yc, xp, yp)
result = area(radius)
return result
The temporary variables radius and result are useful for development and debugging,
butoncetheprogramisworking,wecanmakeitmoreconcisebycomposingthefunction
calls:
def circle_area(xc, yc, xp, yp):
return area(distance(xc, yc, xp, yp))
6.4 Boolean functions
Functionscanreturnbooleans, whichisoftenconvenientforhidingcomplicatedtestsin-
sidefunctions. Forexample:
def is_divisible(x, y):
if x % y == 0:
return True
else:
return False

6.5. Morerecursion 55
It is common to give boolean functions names that sound like yes/no questions;
is_divisiblereturnseitherTrueorFalsetoindicatewhetherxisdivisiblebyy.
Hereisanexample:
| >>> is_divisible(6, | 4)  |     |
| ------------------- | --- | --- |
False
| >>> is_divisible(6, | 3)  |     |
| ------------------- | --- | --- |
True
Theresultofthe==operatorisaboolean,sowecanwritethefunctionmoreconciselyby
returningitdirectly:
| def is_divisible(x, | y):      |     |
| ------------------- | -------- | --- |
| return x            | % y == 0 |     |
Booleanfunctionsareoftenusedinconditionalstatements:
| if is_divisible(x, | y):          |        |
| ------------------ | ------------ | ------ |
| print('x           | is divisible | by y') |
Itmightbetemptingtowritesomethinglike:
| if is_divisible(x, | y) ==        | True:  |
| ------------------ | ------------ | ------ |
| print('x           | is divisible | by y') |
Buttheextracomparisonisunnecessary.
As an exercise, write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or
Falseotherwise.
| 6.5 More | recursion |     |
| -------- | --------- | --- |
WehaveonlycoveredasmallsubsetofPython,butyoumightbeinterestedtoknowthat
this subset is a complete programming language, which means that anything that can be
computedcanbeexpressedinthislanguage.Anyprogrameverwrittencouldberewritten
usingonlythelanguagefeaturesyouhavelearnedsofar(actually,youwouldneedafew
commandstocontroldeviceslikethemouse,disks,etc.,butthat’sall).
Proving that claim is a nontrivial exercise first accomplished by Alan Turing, one of the
firstcomputerscientists(somewouldarguethathewasamathematician,butalotofearly
computer scientists started as mathematicians). Accordingly, it is known as the Turing
Thesis. Foramorecomplete(andaccurate)discussionoftheTuringThesis,Irecommend
MichaelSipser’sbookIntroductiontotheTheoryofComputation.
Togiveyouanideaofwhatyoucandowiththetoolsyouhavelearnedsofar,we’lleval-
uateafewrecursivelydefinedmathematicalfunctions. Arecursivedefinitionissimilarto
acirculardefinition,inthesensethatthedefinitioncontainsareferencetothethingbeing
defined. Atrulycirculardefinitionisnotveryuseful:
vorpal: Anadjectiveusedtodescribesomethingthatisvorpal.
If you saw that definition in the dictionary, you might be annoyed. On the other hand,
if you looked up the definition of the factorial function, denoted with the symbol !, you
mightgetsomethinglikethis:
0! =1
n! = n(n−1)!

56 Chapter6. Fruitfulfunctions
Thisdefinitionsaysthatthefactorialof0is1, andthefactorialofanyothervalue, n, is n
multipliedbythefactorialofn−1.
So3!is3times2!,whichis2times1!,whichis1times0!. Puttingitalltogether,3!equals3
times2times1times1,whichis6.
If you can write a recursive definition of something, you can write a Python program to
evaluateit. Thefirststepistodecidewhattheparametersshouldbe. Inthiscaseitshould
beclearthatfactorialtakesaninteger:
def factorial(n):
Iftheargumenthappenstobe0,allwehavetodoisreturn1:
def factorial(n):
if n == 0:
return 1
Otherwise, and this is the interesting part, we have to make a recursive call to find the
factorialofn−1andthenmultiplyitbyn:
def factorial(n):
if n == 0:
return 1
else:
recurse = factorial(n-1)
result = n * recurse
return result
TheflowofexecutionforthisprogramissimilartotheflowofcountdowninSection5.8. If
wecallfactorialwiththevalue3:
Since3isnot0,wetakethesecondbranchandcalculatethefactorialofn-1...
Since2isnot0,wetakethesecondbranchandcalculatethefactorialofn-1...
Since1isnot0,wetakethesecondbranchandcalculatethefactorial
ofn-1...
Since0equals0,wetakethefirstbranchandreturn1without
makinganymorerecursivecalls.
The return value, 1, is multiplied by n, which is 1, and the result is
returned.
Thereturnvalue,1,ismultipliedbyn,whichis2,andtheresultisreturned.
The return value (2) is multiplied by n, which is 3, and the result, 6, becomes the return
valueofthefunctioncallthatstartedthewholeprocess.
Figure6.1showswhatthestackdiagramlookslikeforthissequenceoffunctioncalls.
The return values are shown being passed back up the stack. In each frame, the return
valueisthevalueofresult,whichistheproductofnandrecurse.
Inthelastframe,thelocalvariablesrecurseandresultdonotexist,becausethebranch
thatcreatesthemdoesnotrun.

6.6. Leapoffaith 57
__main__
6
|     | factorial | n 3 recurse | 2 result | 6   |
| --- | --------- | ----------- | -------- | --- |
2
|     | factorial | n 2 recurse | 1 result | 2   |
| --- | --------- | ----------- | -------- | --- |
1
|     | factorial | n 1 recurse | 1 result | 1   |
| --- | --------- | ----------- | -------- | --- |
1
|          | factorial | n 0        |               |     |
| -------- | --------- | ---------- | ------------- | --- |
|          |           | Figure6.1: | Stackdiagram. |     |
| 6.6 Leap | of faith  |            |               |     |
Following the flow of execution is one way to read programs, but it can quickly become
overwhelming. An alternative is what I call the “leap of faith”. When you come to a
functioncall,insteadoffollowingtheflowofexecution,youassumethatthefunctionworks
correctlyandreturnstherightresult.
Infact,youarealreadypracticingthisleapoffaithwhenyouusebuilt-infunctions. When
youcallmath.cosormath.exp,youdon’texaminethebodiesofthosefunctions.
Youjust
assume that they work because the people who wrote the built-in functions were good
programmers.
Thesameistruewhenyoucalloneofyourownfunctions. Forexample,inSection6.4,we
wroteafunctioncalledis_divisiblethatdetermineswhetheronenumberisdivisibleby
another.Oncewehaveconvincedourselvesthatthisfunctioniscorrect—byexaminingthe
codeandtesting—wecanusethefunctionwithoutlookingatthebodyagain.
The same is true of recursive programs. When you get to the recursive call, instead of
followingtheflowofexecution,youshouldassumethattherecursivecallworks(returns
the correct result) and then ask yourself, “Assuming that I can find the factorial of n−1,
canIcomputethefactorialofn?” Itisclearthatyoucan,bymultiplyingbyn.
Ofcourse,it’sabitstrangetoassumethatthefunctionworkscorrectlywhenyouhaven’t
finishedwritingit,butthat’swhyit’scalledaleapoffaith!
| 6.7 One | more example |     |     |     |
| ------- | ------------ | --- | --- | --- |
Afterfactorial, themostcommonexampleofarecursivelydefinedmathematicalfunc-
| fibonacci, |       |                   | http://en.wikipedia.org/ |     |
| ---------- | ----- | ----------------- | ------------------------ | --- |
| tion is    | which | has the following | definition (see          |     |
wiki/Fibonacci_number):
|     | fibonacci(0) | =0                             |     |     |
| --- | ------------ | ------------------------------ | --- | --- |
|     | fibonacci(1) | =1                             |     |     |
|     | fibonacci(n) | =fibonacci(n−1)+fibonacci(n−2) |     |     |
TranslatedintoPython,itlookslikethis:

| 58  |     |     |     | Chapter6. | Fruitfulfunctions |
| --- | --- | --- | --- | --------- | ----------------- |
def fibonacci(n):
| if  | n == 0: |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
return 0
| elif | n == 1: |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- |
return 1
else:
|     | return fibonacci(n-1) | + fibonacci(n-2) |     |     |     |
| --- | --------------------- | ---------------- | --- | --- | --- |
Ifyoutrytofollowtheflowofexecutionhere,evenforfairlysmallvaluesofn,yourhead
explodes.Butaccordingtotheleapoffaith,ifyouassumethatthetworecursivecallswork
correctly,thenitisclearthatyougettherightresultbyaddingthemtogether.
| 6.8 | Checking types |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- |
Whathappensifwecallfactorialandgiveit1.5asanargument?
>>> factorial(1.5)
| RuntimeError: | Maximum | recursion depth | exceeded |     |     |
| ------------- | ------- | --------------- | -------- | --- | --- |
Thefunctionhasabasecase—whenn
| Itlookslikeaninfiniterecursion. |     | Howcanthatbe? |     |     |     |
| ------------------------------- | --- | ------------- | --- | --- | --- |
== 0. Butifnisnotaninteger,wecanmissthebasecaseandrecurseforever.
n
In the first recursive call, the value of is 0.5. In the next, it is -0.5. From there, it gets
smaller(morenegative),butitwillneverbe0.
factorial
We have two choices. We can try to generalize the function to work with
floating-point numbers, or we can make factorial check the type of its argument. The
firstoptioniscalledthegammafunctionandit’salittlebeyondthescopeofthisbook. So
we’llgoforthesecond.
We can use the built-in function isinstance to verify the type of the argument. While
we’reatit,wecanalsomakesuretheargumentispositive:
def factorial(n):
| if  | not isinstance(n, | int):           |                 |     |     |
| --- | ----------------- | --------------- | --------------- | --- | --- |
|     | print('Factorial  | is only defined | for integers.') |     |     |
return None
| elif | n < 0:           |                |              |             |     |
| ---- | ---------------- | -------------- | ------------ | ----------- | --- |
|      | print('Factorial | is not defined | for negative | integers.') |     |
return None
| elif | n == 0: |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- |
return 1
else:
|     | return n * factorial(n-1) |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- |
The first base case handles nonintegers; the second handles negative integers. In both
None
cases, the program prints an error message and returns to indicate that something
wentwrong:
>>> print(factorial('fred'))
| Factorial | is only defined | for integers. |     |     |     |
| --------- | --------------- | ------------- | --- | --- | --- |
None
>>> print(factorial(-2))
| Factorial | is not defined | for negative | integers. |     |     |
| --------- | -------------- | ------------ | --------- | --- | --- |
None

6.9. Debugging 59
Ifwegetpastbothchecks,weknowthatnisanon-negativeinteger,sowecanprovethat
therecursionterminates.
This program demonstrates a pattern sometimes called a guardian. The first two condi-
tionalsactasguardians,protectingthecodethatfollowsfromvaluesthatmightcausean
error. Theguardiansmakeitpossibletoprovethecorrectnessofthecode.
InSection11.4wewillseeamoreflexiblealternativetoprintinganerrormessage: raising
anexception.
6.9 Debugging
Breakingalargeprogramintosmallerfunctionscreatesnaturalcheckpointsfordebugging.
Ifafunctionisnotworking,therearethreepossibilitiestoconsider:
• Thereissomethingwrongwiththeargumentsthefunctionisgetting;aprecondition
isviolated.
• Thereissomethingwrongwiththefunction;apostconditionisviolated.
• Thereissomethingwrongwiththereturnvalueorthewayitisbeingused.
To rule out the first possibility, you can add a print statement at the beginning of the
function and display the values of the parameters (and maybe their types). Or you can
writecodethatchecksthepreconditionsexplicitly.
print return
If the parameters look good, add a statement before each statement and
displaythereturnvalue.Ifpossible,checktheresultbyhand.Considercallingthefunction
withvaluesthatmakeiteasytochecktheresult(asinSection6.2).
Ifthefunctionseemstobeworking,lookatthefunctioncalltomakesurethereturnvalue
isbeingusedcorrectly(orusedatall!).
Addingprintstatementsatthebeginningandendofafunctioncanhelpmaketheflowof
executionmorevisible. Forexample,hereisaversionoffactorialwithprintstatements:
def factorial(n):
| space = '    | ' * (4 * n)  |     |
| ------------ | ------------ | --- |
| print(space, | 'factorial', | n)  |
| if n == 0:   |              |     |
| print(space, | 'returning   | 1') |
| return       | 1            |     |
else:
| recurse      | = factorial(n-1) |         |
| ------------ | ---------------- | ------- |
| result       | = n * recurse    |         |
| print(space, | 'returning',     | result) |
| return       | result           |         |
spaceisastringofspacecharactersthatcontrolstheindentationoftheoutput.
Hereisthe
resultoffactorial(4):

60 Chapter6. Fruitfulfunctions
factorial 4
factorial 3
factorial 2
factorial 1
factorial 0
returning 1
returning 1
returning 2
returning 6
returning 24
Ifyouareconfusedabouttheflowofexecution,thiskindofoutputcanbehelpful. Ittakes
some time to develop effective scaffolding, but a little bit of scaffolding can save a lot of
debugging.
6.10 Glossary
temporaryvariable: Avariableusedtostoreanintermediatevalueinacomplexcalcula-
tion.
deadcode: Partofaprogramthatcanneverrun, oftenbecauseitappearsafterareturn
statement.
incrementaldevelopment: Aprogramdevelopmentplanintendedtoavoiddebuggingby
addingandtestingonlyasmallamountofcodeatatime.
scaffolding: Code that is used during program development but is not part of the final
version.
guardian: Aprogrammingpatternthatusesaconditionalstatementtocheckforandhan-
dlecircumstancesthatmightcauseanerror.
6.11 Exercises
Exercise6.1. Drawastackdiagramforthefollowingprogram. Whatdoestheprogramprint?
def b(z):
prod = a(z, z)
print(z, prod)
return prod
def a(x, y):
x = x + 1
return x * y
def c(x, y, z):
total = x + y + z
square = b(total)**2
return square

6.11. Exercises 61
x = 1
| y = x +      | 1                     |                   |     |     |
| ------------ | --------------------- | ----------------- | --- | --- |
| print(c(x,   | y+3, x+y))            |                   |     |     |
| Exercise6.2. | TheAckermannfunction, | A(m,n),isdefined: |     |     |

|     |     | n+1 | ifm =0 |     |
| --- | --- | --- | ------ | --- |

|     | A(m,n) = | A(m−1,1) | ifm >0andn | =0  |
| --- | -------- | -------- | ---------- | --- |
A(m−1,A(m,n−1))
|     |     |     | ifm >0andn | >0. |
| --- | --- | --- | ---------- | --- |
Writeafunctionnamedack
Seehttp://en.wikipedia.org/wiki/Ackermann_function.
thatevaluatestheAckermannfunction.Useyourfunctiontoevaluateack(3, 4),whichshouldbe
Whathappensforlargervaluesofmandn?
| 125. |     | Solution: | https://thinkpython.com/code/ |     |
| ---- | --- | --------- | ----------------------------- | --- |
ackermann.py.
Exercise6.3. Apalindromeisawordthatisspelledthesamebackwardandforward,like“noon”
and“redivider”. Recursively,awordisapalindromeifthefirstandlastlettersarethesameandthe
middleisapalindrome.
Thefollowingarefunctionsthattakeastringargumentandreturnthefirst,last,andmiddleletters:
def first(word):
| return | word[0] |     |     |     |
| ------ | ------- | --- | --- | --- |
def last(word):
| return | word[-1] |     |     |     |
| ------ | -------- | --- | --- | --- |
def middle(word):
| return | word[1:-1] |     |     |     |
| ------ | ---------- | --- | --- | --- |
We’llseehowtheyworkinChapter8.
Typethesefunctionsintoafilenamedpalindrome.pyandtestthemout.
| 1.  |     |     |     | Whathappensif |
| --- | --- | --- | --- | ------------- |
middle
you call with a string with two letters? One letter? What about the empty string,
whichiswritten''andcontainsnoletters?
2. Writeafunctioncalledis_palindromethattakesastringargumentandreturnsTrueifit
isapalindromeandFalseotherwise. Rememberthatyoucanusethebuilt-infunctionlen
tocheckthelengthofastring.
Solution: https://thinkpython.com/code/palindrome_soln.py.
Exercise6.4. Anumber, a, isapowerof b ifitisdivisibleby b and a/b isapowerof b. Writea
functioncalledis_powerthattakesparametersaandbandreturnsTrueifaisapowerofb.Note:
youwillhavetothinkaboutthebasecase.
Exercise 6.5. The greatest common divisor (GCD) of a and b is the largest number that divides
bothofthemwithnoremainder.
OnewaytofindtheGCDoftwonumbersisbasedontheobservationthatifristheremainderwhen
aisdividedbyb,thengcd(a,b) = gcd(b,r). Asabasecase,wecanusegcd(a,0) =
a.
Writeafunctioncalledgcdthattakesparametersaandbandreturnstheirgreatestcommondivisor.
Credit: ThisexerciseisbasedonanexamplefromAbelsonandSussman’sStructureandInterpre-
tationofComputerPrograms.

| 62  | Chapter6. | Fruitfulfunctions |
| --- | --------- | ----------------- |

Chapter 7
Iteration
Thischapterisaboutiteration,whichistheabilitytorunablockofstatementsrepeatedly.
Wesawakindofiteration, usingrecursion, inSection5.8. Wesawanotherkind, usinga
forloop,inSection4.2. Inthischapterwe’llseeyetanotherkind,usingawhilestatement.
ButfirstIwanttosayalittlemoreaboutvariableassignment.
7.1 Reassignment
As you may have discovered, it is legal to make more than one assignment to the same
variable. A new assignment makes an existing variable refer to a new value (and stop
referringtotheoldvalue).
>>> x = 5
>>> x
5
>>> x = 7
>>> x
7
Thefirsttimewedisplayx,itsvalueis5;thesecondtime,itsvalueis7.
Figure7.1showswhatreassignmentlookslikeinastatediagram.
At this point I want to address a common source of confusion. Because Python uses the
equalsign(=)forassignment,itistemptingtointerpretastatementlikea = basamathe-
maticalpropositionofequality;thatis,theclaimthataandbareequal. Butthisinterpre-
tationiswrong.
First, equality is a symmetric relationship and assignment is not. For example, in math-
ematics, if a = 7 then 7 = a. But in Python, the statement a = 7 is legal and 7 = a is
not.
Also, in mathematics, a proposition of equality is either true or false for all time. If a =
b now, then a will always equal b. In Python, an assignment statement can make two
variablesequal,buttheydon’thavetostaythatway:

| 64  |     |     |     | Chapter7. | Iteration |
| --- | --- | --- | --- | --------- | --------- |
5
x
7
|         |           | Figure7.1:      | Statediagram. |     |     |
| ------- | --------- | --------------- | ------------- | --- | --- |
| >>> a = | 5         |                 |               |     |     |
| >>> b = | a # a and | b are now equal |               |     |     |
| >>> a = | 3 # a and | b are no longer | equal         |     |     |
>>> b
5
The third line changes the value of a but does not change the value of b, so they are no
longerequal.
Reassigningvariablesis oftenuseful, butyoushould useitwithcaution. Ifthevalues of
variableschangefrequently,itcanmakethecodedifficulttoreadanddebug.
| 7.2 Updating | variables |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
Acommonkindofreassignmentisanupdate,wherethenewvalueofthevariabledepends
ontheold.
| >>> x = | x + 1 |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- |
Thismeans“getthecurrentvalueofx,addone,andthenupdatexwiththenewvalue.”
Ifyoutrytoupdateavariablethatdoesn’texist,yougetanerror,becausePythonevaluates
therightsidebeforeitassignsavaluetox:
| >>> x =    | x + 1    |                |     |     |     |
| ---------- | -------- | -------------- | --- | --- | --- |
| NameError: | name 'x' | is not defined |     |     |     |
Before you can update a variable, you have to initialize it, usually with a simple assign-
ment:
| >>> x = | 0     |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- |
| >>> x = | x + 1 |     |     |     |     |
Updatingavariablebyadding1iscalledanincrement;subtracting1iscalledadecrement.
| 7.3 The | while | statement |     |     |     |
| ------- | ----- | --------- | --- | --- | --- |
Computersareoftenusedtoautomaterepetitivetasks.Repeatingidenticalorsimilartasks
without making errors is something that computers do well and people do poorly. In a
computerprogram,repetitionisalsocallediteration.
Wehavealreadyseentwofunctions,countdownandprint_n,thatiterateusingrecursion.
Becauseiterationissocommon,Pythonprovideslanguagefeaturestomakeiteasier. One
| istheforstatementwesawinSection4.2. |     |     | We’llgetbacktothatlater. |     |     |
| ----------------------------------- | --- | --- | ------------------------ | --- | --- |
Anotheristhewhilestatement.Hereisaversionofcountdownthatusesawhilestatement:

7.3. Thewhilestatement 65
def countdown(n):
while n > 0:
print(n)
n = n - 1
print('Blastoff!')
YoucanalmostreadthewhilestatementasifitwereEnglish. Itmeans,“Whilenisgreater
than0,displaythevalueofnandthendecrementn. Whenyougetto0,displaytheword
Blastoff!”
Moreformally,hereistheflowofexecutionforawhilestatement:
1. Determinewhethertheconditionistrueorfalse.
2. Iffalse,exitthewhilestatementandcontinueexecutionatthenextstatement.
3. Iftheconditionistrue,runthebodyandthengobacktostep1.
Thistypeofflowiscalledaloopbecausethethirdsteploopsbackaroundtothetop.
Thebodyoftheloopshouldchangethevalueofoneormorevariablessothatthecondition
becomesfalseeventuallyandtheloopterminates. Otherwisetheloopwillrepeatforever,
whichiscalledaninfiniteloop. Anendlesssourceofamusementforcomputerscientists
is the observation that the directions on shampoo, “Lather, rinse, repeat”, are an infinite
loop.
Inthecaseofcountdown,wecanprovethattheloopterminates:ifniszeroornegative,the
loop never runs. Otherwise, n gets smaller each time through the loop, so eventually we
havetogetto0.
Forsomeotherloops,itisnotsoeasytotell. Forexample:
def sequence(n):
while n != 1:
print(n)
if n % 2 == 0: # n is even
n = n / 2
else: # n is odd
n = n*3 + 1
The condition for this loop is n != 1, so the loop will continue until n is 1, which makes
theconditionfalse.
Eachtimethroughtheloop,theprogramoutputsthevalueofnandthencheckswhether
itisevenorodd. Ifitiseven,nisdividedby2. Ifitisodd,thevalueofnisreplacedwith
n*3 + 1. For example, if the argument passed to sequence is 3, the resulting values of n
are3,10,5,16,8,4,2,1.
Sincensometimesincreasesandsometimesdecreases,thereisnoobviousproofthatnwill
everreach1,orthattheprogramterminates. Forsomeparticularvaluesofn,wecanprove
termination. For example, if the starting value is a power of two, n will be even every
timethroughtheloopuntilitreaches1. Thepreviousexampleendswithsuchasequence,
startingwith16.
The hard question is whether we can prove that this program terminates for all posi-
tive values of n. So far, no one has been able to prove it or disprove it! (See http:
//en.wikipedia.org/wiki/Collatz_conjecture.)

66 Chapter7. Iteration
As an exercise, rewrite the function print_n from Section 5.8 using iteration instead of
recursion.
7.4 break
Sometimesyoudon’tknowit’stimetoendaloopuntilyougethalfwaythroughthebody.
Inthatcaseyoucanusethebreakstatementtojumpoutoftheloop.
Forexample,supposeyouwanttotakeinputfromtheuseruntiltheytypedone.Youcould
write:
while True:
line = input('> ')
if line == 'done':
break
print(line)
print('Done!')
The loop condition is True, which is always true, so the loop runs until it hits the break
statement.
Each time through, it prompts the user with an angle bracket. If the user types done, the
breakstatementexitstheloop.Otherwisetheprogramechoeswhatevertheusertypesand
goesbacktothetopoftheloop. Here’sasamplerun:
> not done
not done
> done
Done!
Thiswayofwritingwhileloopsiscommonbecauseyoucanchecktheconditionanywhere
intheloop(notjustatthetop)andyoucanexpressthestopconditionaffirmatively(“stop
whenthishappens”)ratherthannegatively(“keepgoinguntilthathappens”).
7.5 Square roots
Loopsareoftenusedinprogramsthatcomputenumericalresultsbystartingwithanap-
proximateansweranditerativelyimprovingit.
Forexample, onewayofcomputingsquarerootsisNewton’smethod. Supposethatyou
wanttoknowthesquarerootof a. Ifyoustartwithalmostanyestimate, x,youcancom-
puteabetterestimatewiththefollowingformula:
x+a/x
y =
2
Forexample,ifais4andxis3:
>>> a = 4
>>> x = 3
>>> y = (x + a/x) / 2
>>> y
2.16666666667

7.6. Algorithms 67
√
Theresultisclosertothecorrectanswer( 4 = 2). Ifwerepeattheprocesswiththenew
estimate,itgetsevencloser:
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00641025641
Afterafewmoreupdates,theestimateisalmostexact:
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00001024003
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00000000003
Ingeneralwedon’tknowaheadoftimehowmanystepsittakestogettotherightanswer,
butweknowwhenwegettherebecausetheestimatestopschanging:
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0
When y == x, we can stop. Here is a loop that starts with an initial estimate, x, and im-
provesituntilitstopschanging:
while True:
print(x)
y = (x + a/x) / 2
if y == x:
break
x = y
Formostvaluesofathisworksfine, butingeneralitisdangeroustotestfloatequality.
Floating-pointvaluesareonlyapproximatelyright: mostrationalnumbers, like1/3, and
√
irrationalnumbers,like 2,can’tberepresentedexactlywithafloat.
Ratherthancheckingwhetherxandyareexactlyequal,itissafertousethebuilt-infunc-
tionabstocomputetheabsolutevalue,ormagnitude,ofthedifferencebetweenthem:
if abs(y-x) < epsilon:
break
Whereepsilonhasavaluelike0.0000001thatdetermineshowcloseiscloseenough.
7.6 Algorithms
Newton’smethodisanexampleofanalgorithm: itisamechanicalprocessforsolvinga
categoryofproblems(inthiscase,computingsquareroots).

68 Chapter7. Iteration
To understand what an algorithm is, it might help to start with something that is not an
algorithm. Whenyoulearnedtomultiplysingle-digitnumbers,youprobablymemorized
the multiplication table. In effect, you memorized 100 specific solutions. That kind of
knowledgeisnotalgorithmic.
But if you were “lazy”, you might have learned a few tricks. For example, to find the
product of n and 9, you can write n−1 as the first digit and 10−n as the second digit.
This trick is a general solution for multiplying any single-digit number by 9. That’s an
algorithm!
Similarly,thetechniquesyoulearnedforadditionwithcarrying,subtractionwithborrow-
ing, and long division are all algorithms. One of the characteristics of algorithms is that
they do not require any intelligence to carry out. They are mechanical processes where
eachstepfollowsfromthelastaccordingtoasimplesetofrules.
Executing algorithms is boring, but designing them is interesting, intellectually challeng-
ing,andacentralpartofcomputerscience.
Some of the things that people do naturally, without difficulty or conscious thought, are
thehardesttoexpressalgorithmically. Understandingnaturallanguageisagoodexample.
Wealldoit,butsofarnoonehasbeenabletoexplainhowwedoit,atleastnotintheform
ofanalgorithm.
7.7 Debugging
Asyoustartwritingbiggerprograms,youmightfindyourselfspendingmoretimedebug-
ging. Morecodemeansmorechancestomakeanerrorandmoreplacesforbugstohide.
One way to cut your debugging time is “debugging by bisection”. For example, if there
are100linesinyourprogramandyoucheckthemoneatatime,itwouldtake100steps.
Instead,trytobreaktheprobleminhalf. Lookatthemiddleoftheprogram,ornearit,for
anintermediatevalueyoucancheck. Addaprintstatement(orsomethingelsethathasa
verifiableeffect)andruntheprogram.
Ifthemid-pointcheckisincorrect,theremustbeaprobleminthefirsthalfoftheprogram.
Ifitiscorrect,theproblemisinthesecondhalf.
Everytimeyouperformachecklikethis,youhalvethenumberoflinesyouhavetosearch.
Aftersixsteps(whichisfewerthan100),youwouldbedowntooneortwolinesofcode,
atleastintheory.
Inpracticeitisnotalwaysclearwhatthe“middleoftheprogram”isandnotalwayspos-
sibletocheckit. Itdoesn’tmakesensetocountlinesandfindtheexactmidpoint. Instead,
thinkaboutplacesintheprogramwheretheremightbeerrorsandplaceswhereitiseasy
to put a check. Then choose a spot where you think the chances are about the same that
thebugisbeforeorafterthecheck.
7.8 Glossary
reassignment: Assigninganewvaluetoavariablethatalreadyexists.

7.9. Exercises 69
update: Anassignmentwherethenewvalueofthevariabledependsontheold.
initialization: Anassignmentthatgivesaninitialvaluetoavariablethatwillbeupdated.
increment: Anupdatethatincreasesthevalueofavariable(oftenbyone).
| decrement: Anupdatethatdecreasesthevalueofavariable. |     |     |
| ---------------------------------------------------- | --- | --- |
iteration: Repeated execution of a set of statements using either a recursive function call
oraloop.
| infiniteloop: Aloopinwhichtheterminatingconditionisneversatisfied. |     |     |
| ------------------------------------------------------------------ | --- | --- |
algorithm: Ageneralprocessforsolvingacategoryofproblems.
7.9 Exercises
Exercise7.1. CopytheloopfromSection7.5andencapsulateitinafunctioncalledmysqrtthat
takesaasaparameter,choosesareasonablevalueofx,andreturnsanestimateofthesquarerootof
a.
Totestit,writeafunctionnamedtest_square_rootthatprintsatablelikethis:
| a mysqrt(a)       | math.sqrt(a)  | diff              |
| ----------------- | ------------- | ----------------- |
| - ---------       | ------------  | ----              |
| 1.0 1.0           | 1.0           | 0.0               |
| 2.0 1.41421356237 | 1.41421356237 | 2.22044604925e-16 |
| 3.0 1.73205080757 | 1.73205080757 | 0.0               |
| 4.0 2.0           | 2.0           | 0.0               |
| 5.0 2.2360679775  | 2.2360679775  | 0.0               |
| 6.0 2.44948974278 | 2.44948974278 | 0.0               |
| 7.0 2.64575131106 | 2.64575131106 | 0.0               |
| 8.0 2.82842712475 | 2.82842712475 | 4.4408920985e-16  |
| 9.0 3.0           | 3.0           | 0.0               |
acomputedwithmysqrt;
| Thefirstcolumnisanumber, | a;thesecondcolumnisthesquarerootof |     |
| ------------------------ | ---------------------------------- | --- |
thethirdcolumnisthesquarerootcomputedbymath.sqrt;thefourthcolumnistheabsolutevalue
ofthedifferencebetweenthetwoestimates.
eval
Exercise 7.2. The built-in function takes a string and evaluates it using the Python inter-
preter. Forexample:
| >>> eval('1 + 2 | * 3') |     |
| --------------- | ----- | --- |
7
| >>> import math |     |     |
| --------------- | --- | --- |
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Writeafunctioncalledeval_loopthatiterativelypromptstheuser,takestheresultinginputand
evaluatesitusingeval,andprintstheresult.
Itshouldcontinueuntiltheuserenters'done',andthenreturnthevalueofthelastexpressionit
evaluated.

70 Chapter7. Iteration
Exercise7.3. ThemathematicianSrinivasaRamanujanfoundaninfiniteseriesthatcanbeusedto
generateanumericalapproximationof1/π:
√
∞
1 2 2 ∑ (4k)!(1103+26390k)
=
π 9801 (k!)43964k
k=0
Writeafunctioncalledestimate_pithatusesthisformulatocomputeandreturnanestimateof
π. Itshoulduseawhilelooptocomputetermsofthesummationuntilthelasttermissmallerthan
1e-15(whichisPythonnotationfor10−15). Youcanchecktheresultbycomparingittomath.pi.
Solution: https://thinkpython.com/code/pi.py.

Chapter 8
Strings
Stringsarenotlikeintegers,floats,andbooleans. Astringisasequence,whichmeansitis
anorderedcollectionofothervalues.Inthischapteryou’llseehowtoaccessthecharacters
thatmakeupastring,andyou’lllearnaboutsomeofthemethodsstringsprovide.
8.1 A string is a sequence
A string is a sequence of characters. You can access the characters one at a time with the
bracketoperator:
>>> fruit = 'banana'
>>> letter = fruit[1]
Thesecondstatementselectscharacternumber1fromfruitandassignsittoletter.
The expression in brackets is called an index. The index indicates which character in the
sequenceyouwant(hencethename).
Butyoumightnotgetwhatyouexpect:
>>> letter
'a'
For most people, the first letter of 'banana' is b, not a. But for computer scientists, the
indexisanoffsetfromthebeginningofthestring,andtheoffsetofthefirstletteriszero.
>>> letter = fruit[0]
>>> letter
'b'
Sobisthe0thletter(“zero-eth”)of'banana',aisthe1thletter(“one-eth”),andnisthe2th
letter(“two-eth”).
Asanindexyoucanuseanexpressionthatcontainsvariablesandoperators:
>>> i = 1
>>> fruit[i]
'a'
>>> fruit[i+1]
'n'

| 72  |     |     | Chapter8. | Strings |
| --- | --- | --- | --------- | ------- |
Butthevalueoftheindexhastobeaninteger. Otherwiseyouget:
| >>> letter | = fruit[1.5]   |                  |     |     |
| ---------- | -------------- | ---------------- | --- | --- |
| TypeError: | string indices | must be integers |     |     |
8.2 len
lenisabuilt-infunctionthatreturnsthenumberofcharactersinastring:
| >>> fruit | = 'banana' |     |     |     |
| --------- | ---------- | --- | --- | --- |
>>> len(fruit)
6
Togetthelastletterofastring,youmightbetemptedtotrysomethinglikethis:
| >>> length  | = len(fruit)    |              |     |     |
| ----------- | --------------- | ------------ | --- | --- |
| >>> last    | = fruit[length] |              |     |     |
| IndexError: | string index    | out of range |     |     |
ThereasonfortheIndexErroristhatthereisnoletterin’banana’withtheindex6. Since
we started counting at zero, the six letters are numbered 0 to 5. To get the last character,
youhavetosubtract1fromlength:
| >>> last | = fruit[length-1] |     |     |     |
| -------- | ----------------- | --- | --- | --- |
>>> last
'a'
Or you can use negative indices, which count backward from the end of the string. The
expressionfruit[-1]yieldsthelastletter,fruit[-2]yieldsthesecondtolast,andsoon.
| 8.3 Traversal | with | a for loop |     |     |
| ------------- | ---- | ---------- | --- | --- |
Alotofcomputationsinvolveprocessingastringonecharacteratatime. Oftentheystart
at the beginning, select each character in turn, do something to it, and continue until the
end. Thispatternofprocessingiscalledatraversal. Onewaytowriteatraversaliswitha
whileloop:
| index =     | 0              |     |     |     |
| ----------- | -------------- | --- | --- | --- |
| while index | < len(fruit):  |     |     |     |
| letter      | = fruit[index] |     |     |     |
print(letter)
| index | = index + 1 |     |     |     |
| ----- | ----------- | --- | --- | --- |
Thislooptraversesthestringanddisplayseachletteronalinebyitself.Theloopcondition
isindex < len(fruit),sowhenindexisequaltothelengthofthestring,theconditionis
false,andthebodyoftheloopdoesn’trun. Thelastcharacteraccessedistheonewiththe
indexlen(fruit)-1,whichisthelastcharacterinthestring.
Asanexercise,writeafunctionthattakesastringasanargumentanddisplaystheletters
backward,oneperline.
Anotherwaytowriteatraversaliswithaforloop:
| for letter | in fruit: |     |     |     |
| ---------- | --------- | --- | --- | --- |
print(letter)

8.4. Stringslices 73
’ b a n a n a ’
fruit
index 0 1 2 3 4 5 6
Figure8.1: Sliceindices.
Each time through the loop, the next character in the string is assigned to the variable
letter. Theloopcontinuesuntilnocharactersareleft.
The following example shows how to use concatenation (string addition) and a for loop
to generate an abecedarian series (that is, in alphabetical order). In Robert McCloskey’s
bookMakeWayforDucklings,thenamesoftheducklingsareJack,Kack,Lack,Mack,Nack,
Ouack,Pack,andQuack. Thisloopoutputsthesenamesinorder:
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
print(letter + suffix)
Theoutputis:
Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack
Of course, that’s not quite right because “Ouack” and “Quack” are misspelled. As an
exercise,modifytheprogramtofixthiserror.
8.4 String slices
Asegmentofastringiscalledaslice. Selectingasliceissimilartoselectingacharacter:
>>> s = 'Monty Python'
>>> s[0:5]
'Monty'
>>> s[6:12]
'Python'
Theoperator[n:m]returnsthepartofthestringfromthe“n-eth”charactertothe“m-eth”
character, includingthefirstbutexcludingthelast. Thisbehavioriscounterintuitive, but
itmighthelptoimaginetheindicespointingbetweenthecharacters,asinFigure8.1.
Ifyouomitthefirstindex(beforethecolon),theslicestartsatthebeginningofthestring.
Ifyouomitthesecondindex,theslicegoestotheendofthestring:
>>> fruit = 'banana'
>>> fruit[:3]

| 74  |     |     |     | Chapter8. | Strings |
| --- | --- | --- | --- | --------- | ------- |
'ban'
>>> fruit[3:]
'ana'
Ifthefirstindexisgreaterthanorequaltothesecondtheresultisanemptystring,repre-
sentedbytwoquotationmarks:
| >>> fruit | = 'banana' |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- |
>>> fruit[3:3]
''
Anemptystringcontainsnocharactersandhaslength0,butotherthanthat,itisthesame
asanyotherstring.
Continuingthisexample,whatdoyouthinkfruit[:] means? Tryitandsee.
| 8.5 Strings | are | immutable |     |     |     |
| ----------- | --- | --------- | --- | --- | --- |
Itistemptingtousethe[]operatorontheleftsideofanassignment,withtheintentionof
| changingacharacterinastring. |              | Forexample:      |                 |     |     |
| ---------------------------- | ------------ | ---------------- | --------------- | --- | --- |
| >>> greeting                 | = 'Hello,    | world!'          |                 |     |     |
| >>> greeting[0]              | = 'J'        |                  |                 |     |     |
| TypeError:                   | 'str' object | does not support | item assignment |     |     |
The “object” in this case is the string and the “item” is the character you tried to assign.
For now, an object is the same thing as a value, but we will refine that definition later
(Section10.10).
The reason for the error is that strings are immutable, which means you can’t change an
existingstring. Thebestyoucandoiscreateanewstringthatisavariationontheoriginal:
| >>> greeting     | = 'Hello, | world!'        |     |     |     |
| ---------------- | --------- | -------------- | --- | --- | --- |
| >>> new_greeting | = 'J'     | + greeting[1:] |     |     |     |
>>> new_greeting
| 'Jello, | world!' |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
Thisexampleconcatenatesanewfirstletterontoasliceofgreeting.
Ithasnoeffectonthe
originalstring.
8.6 Searching
Whatdoesthefollowingfunctiondo?
| def find(word, | letter):           |            |     |     |     |
| -------------- | ------------------ | ---------- | --- | --- | --- |
| index          | = 0                |            |     |     |     |
| while          | index < len(word): |            |     |     |     |
|                | if word[index]     | == letter: |     |     |     |
|                | return index       |            |     |     |     |
|                | index = index      | + 1        |     |     |     |
| return         | -1                 |            |     |     |     |

8.7. Loopingandcounting 75
Inasense,findistheinverseofthe[]operator. Insteadoftakinganindexandextracting
thecorrespondingcharacter, ittakesacharacterandfindstheindexwherethatcharacter
appears. Ifthecharacterisnotfound,thefunctionreturns-1.
Thisisthefirstexamplewehaveseenofareturnstatementinsidealoop. Ifword[index]
== letter,thefunctionbreaksoutoftheloopandreturnsimmediately.
If the character doesn’t appear in the string, the program exits the loop normally and re-
turns-1.
Thispatternofcomputation—traversingasequenceandreturningwhenwefindwhatwe
arelookingfor—iscalledasearch.
As an exercise, modify find so that it has a third parameter, the index in word where it
shouldstartlooking.
8.7 Looping and counting
Thefollowingprogramcountsthenumberoftimestheletteraappearsinastring:
word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)
Thisprogramdemonstratesanotherpatternofcomputationcalledacounter. Thevariable
countisinitializedto0andthenincrementedeachtimeanaisfound.Whentheloopexits,
countcontainstheresult—thetotalnumberofa’s.
Asanexercise,encapsulatethiscodeinafunctionnamedcount,andgeneralizeitsothat
itacceptsthestringandtheletterasarguments.
Then rewrite the function so that instead of traversing the string, it uses the three-
parameterversionoffindfromtheprevioussection.
8.8 String methods
Stringsprovidemethodsthatperformavarietyofusefuloperations. Amethodissimilar
to a function—it takes arguments and returns a value—but the syntax is different. For
example, the method upper takes a string and returns a new string with all uppercase
letters.
Insteadofthefunctionsyntaxupper(word),itusesthemethodsyntaxword.upper().
>>> word = 'banana'
>>> new_word = word.upper()
>>> new_word
'BANANA'

76 Chapter8. Strings
This form of dot notation specifies the name of the method, upper, and the name of the
string to apply the method to, word. The empty parentheses indicate that this method
takesnoarguments.
A method call is called an invocation; in this case, we would say that we are invoking
upperonword.
As it turns out, there is a string method named find that is remarkably similar to the
functionwewrote:
>>> word = 'banana'
>>> index = word.find('a')
>>> index
1
Inthisexample,weinvokefindonwordandpasstheletterwearelookingforasaparam-
eter.
Actually,thefindmethodismoregeneralthanourfunction;itcanfindsubstrings,notjust
characters:
>>> word.find('na')
2
Bydefault,findstartsatthebeginningofthestring,butitcantakeasecondargument,the
indexwhereitshouldstart:
>>> word.find('na', 3)
4
Thisisanexampleofanoptionalargument;findcanalsotakeathirdargument,theindex
whereitshouldstop:
>>> name = 'bob'
>>> name.find('b', 1, 2)
-1
Thissearchfailsbecausebdoesnotappearintheindexrangefrom1to2,notincluding2.
Searchingupto,butnotincluding,thesecondindexmakesfindconsistentwiththeslice
operator.
8.9 The in operator
The word in is a boolean operator that takes two strings and returns True if the first ap-
pearsasasubstringinthesecond:
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
For example, the following function prints all the letters from word1 that also appear in
word2:
def in_both(word1, word2):
for letter in word1:
if letter in word2:
print(letter)

8.10. Stringcomparison 77
With well-chosen variable names, Python sometimes reads like English. You could read
thisloop,“for(each)letterin(thefirst)word,if(the)letter(appears)in(thesecond)word,
print(the)letter.”
Here’swhatyougetifyoucompareapplesandoranges:
| >>> in_both('apples', |     | 'oranges') |     |     |
| --------------------- | --- | ---------- | --- | --- |
a
e
s
| 8.10                                 | String comparison |            |                            |     |
| ------------------------------------ | ----------------- | ---------- | -------------------------- | --- |
| Therelationaloperatorsworkonstrings. |                   |            | Toseeiftwostringsareequal: |     |
| if word                              | == 'banana':      |            |                            |     |
| print('All                           | right,            | bananas.') |                            |     |
Otherrelationaloperationsareusefulforputtingwordsinalphabeticalorder:
| if word     | < 'banana': |            |                 |           |
| ----------- | ----------- | ---------- | --------------- | --------- |
| print('Your | word,       | ' + word + | ', comes before | banana.') |
| elif word   | > 'banana': |            |                 |           |
| print('Your | word,       | ' + word + | ', comes after  | banana.') |
else:
| print('All | right, | bananas.') |     |     |
| ---------- | ------ | ---------- | --- | --- |
Pythondoesnothandleuppercaseandlowercaselettersthesamewaypeopledo. Allthe
uppercaseletterscomebeforeallthelowercaseletters,so:
| Your word, | Pineapple, | comes before | banana. |     |
| ---------- | ---------- | ------------ | ------- | --- |
Acommonwaytoaddressthisproblemistoconvertstringstoastandardformat,suchas
all lowercase, before performing the comparison. Keep that in mind in case you have to
defendyourselfagainstamanarmedwithaPineapple.
8.11 Debugging
Whenyouuseindicestotraversethevaluesinasequence,itistrickytogetthebeginning
andendofthetraversalright. Hereisafunctionthatissupposedtocomparetwowords
andreturnTrueifoneofthewordsisthereverseoftheother,butitcontainstwoerrors:
| def is_reverse(word1, |     | word2):     |     |     |
| --------------------- | --- | ----------- | --- | --- |
| if len(word1)         | !=  | len(word2): |     |     |
return False
| i =   | 0           |              |     |     |
| ----- | ----------- | ------------ | --- | --- |
| j =   | len(word2)  |              |     |     |
| while | j > 0:      |              |     |     |
|       | if word1[i] | != word2[j]: |     |     |
|       | return      | False        |     |     |
i = i+1

| 78  |     |     | Chapter8. | Strings |
| --- | --- | --- | --------- | ------- |
j = j-1
| return | True |     |     |     |
| ------ | ---- | --- | --- | --- |
Thefirstifstatementcheckswhetherthewordsarethesamelength.
Ifnot,wecanreturn
Falseimmediately.
Otherwise,fortherestofthefunction,wecanassumethatthewords
arethesamelength. ThisisanexampleoftheguardianpatterninSection6.8.
i and j are indices: i traverses word1 forward while j traverses word2 backward. If we
findtwolettersthatdon’tmatch,wecanreturnFalseimmediately.
Ifwegetthroughthe
wholeloopandallthelettersmatch,wereturnTrue.
Ifwetestthisfunctionwiththewords“pots”and“stop”,weexpectthereturnvalueTrue,
butwegetanIndexError:
| >>> is_reverse('pots', |     | 'stop') |     |     |
| ---------------------- | --- | ------- | --- | --- |
...
| File "reverse.py", | line         | 15, in is_reverse |     |     |
| ------------------ | ------------ | ----------------- | --- | --- |
| if word1[i]        | != word2[j]: |                   |     |     |
| IndexError:        | string index | out of range      |     |     |
Fordebuggingthiskindoferror,myfirstmoveistoprintthevaluesoftheindicesimme-
diatelybeforethelinewheretheerrorappears.
| while    | j > 0:      |              |     |     |
| -------- | ----------- | ------------ | --- | --- |
| print(i, | j)          | # print here |     |     |
| if       | word1[i] != | word2[j]:    |     |     |
return False
i = i+1
j = j-1
NowwhenIruntheprogramagain,Igetmoreinformation:
| >>> is_reverse('pots', |     | 'stop') |     |     |
| ---------------------- | --- | ------- | --- | --- |
0 4
...
| IndexError: | string index | out of range |     |     |
| ----------- | ------------ | ------------ | --- | --- |
j
The first time through the loop, the value of is 4, which is out of range for the
string 'pots'. The index of the last character is 3, so the initial value for j should be
len(word2)-1.
IfIfixthaterrorandruntheprogramagain,Iget:
| >>> is_reverse('pots', |     | 'stop') |     |     |
| ---------------------- | --- | ------- | --- | --- |
0 3
1 2
2 1
True
Thistimewegettherightanswer,butitlookslikethelooponlyranthreetimes,whichis
suspicious. Togetabetterideaofwhatishappening,itisusefultodrawastatediagram.
Duringthefirstiteration,theframeforis_reverseisshowninFigure8.2.
Itooksomelicensebyarrangingthevariablesintheframeandaddingdottedlinestoshow
thatthevaluesofiandjindicatecharactersinword1andword2.
i j
Starting with this diagram, run the program on paper, changing the values of and
| duringeachiteration. | Findandfixtheseconderrorinthisfunction. |     |     |     |
| -------------------- | --------------------------------------- | --- | --- | --- |

8.12. Glossary 79
word1 ’pots’ word2 ’stop’
i 0 j 3
Figure8.2: Statediagram.
8.12 Glossary
object: Something a variable can refer to. For now, you can use “object” and “value”
interchangeably.
sequence: An ordered collection of values where each value is identified by an integer
index.
item: Oneofthevaluesinasequence.
index: Anintegervalueusedtoselectaniteminasequence,suchasacharacterinastring.
InPythonindicesstartfrom0.
slice: Apartofastringspecifiedbyarangeofindices.
emptystring: A string with no characters and length 0, represented by two quotation
marks.
immutable: Thepropertyofasequencewhoseitemscannotbechanged.
traverse: To iterate through the items in a sequence, performing a similar operation on
each.
search: Apatternoftraversalthatstopswhenitfindswhatitislookingfor.
counter: A variable used to count something, usually initialized to zero and then incre-
mented.
invocation: Astatementthatcallsamethod.
optionalargument: Afunctionormethodargumentthatisnotrequired.
8.13 Exercises
Exercise8.1. Readthedocumentationofthestringmethodsathttp://docs.python.org/3/
library/stdtypes.html#string-methods.Youmightwanttoexperimentwithsomeofthem
tomakesureyouunderstandhowtheywork. stripandreplaceareparticularlyuseful.
The documentation uses a syntax that might be confusing. For example, in
find(sub[, start[, end]]),thebracketsindicateoptionalarguments. Sosubisrequired,but
startisoptional,andifyouincludestart,thenendisoptional.
Exercise8.2. ThereisastringmethodcalledcountthatissimilartothefunctioninSection8.7.
Read the documentation of this method and write an invocation that counts the number of a’s in
'banana'.
Exercise8.3. Astringslicecantakeathirdindexthatspecifiesthe“stepsize”;thatis,thenumber
ofspacesbetweensuccessivecharacters. Astepsizeof2meanseveryothercharacter;3meansevery
third,etc.

80 Chapter8. Strings
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
Astepsizeof-1goesthroughthewordbackwards,sotheslice[::-1]generatesareversedstring.
Usethisidiomtowriteaone-lineversionofis_palindromefromExercise6.3.
Exercise 8.4. The following functions are all intended to check whether a string contains any
lowercaseletters,butatleastsomeofthemarewrong. Foreachfunction,describewhatthefunction
actuallydoes(assumingthattheparameterisastring).
def any_lowercase1(s):
for c in s:
if c.islower():
return True
else:
return False
def any_lowercase2(s):
for c in s:
if 'c'.islower():
return 'True'
else:
return 'False'
def any_lowercase3(s):
for c in s:
flag = c.islower()
return flag
def any_lowercase4(s):
flag = False
for c in s:
flag = flag or c.islower()
return flag
def any_lowercase5(s):
for c in s:
if not c.islower():
return False
return True
Exercise8.5. ACaesarcypherisaweakformofencryptionthatinvolves“rotating”eachletterby
afixednumberofplaces. Torotatealettermeanstoshiftitthroughthealphabet,wrappingaround
tothebeginningifnecessary,so’A’rotatedby3is’D’and’Z’rotatedby1is’A’.
Torotateaword,rotateeachletterbythesameamount. Forexample,“cheer”rotatedby7is“jolly”
and“melon”rotatedby-10is“cubed”. Inthemovie2001: ASpaceOdyssey,theshipcomputer
iscalledHAL,whichisIBMrotatedby-1.
Writeafunctioncalledrotate_wordthattakesastringandanintegerasparameters,andreturns
anewstringthatcontainsthelettersfromtheoriginalstringrotatedbythegivenamount.
Youmightwanttousethebuilt-infunctionord,whichconvertsacharactertoanumericcode,and

8.13. Exercises 81
chr,whichconvertsnumericcodestocharacters. Lettersofthealphabetareencodedinalphabetical
order,soforexample:
>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
lettersaredifferent.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar
cypher with rotation 13. If you are not easily offended, find and decode some of them. Solution:
https://thinkpython.com/code/rotate.py.

| 82  | Chapter8. | Strings |
| --- | --------- | ------- |

Chapter 9
Case study: word play
This chapter presents the second case study, which involves solving word puzzles by
searchingforwordsthathavecertainproperties. Forexample,we’llfindthelongestpalin-
dromes in English and search for words whose letters appear in alphabetical order. And
Iwillpresentanotherprogramdevelopmentplan: reductiontoapreviouslysolvedprob-
lem.
9.1 Reading word lists
For the exercises in this chapter we need a list of English words. There are lots of word
listsavailableontheWeb,buttheonemostsuitableforourpurposeisoneofthewordlists
collected and contributed to the public domain by Grady Ward as part of the Moby lexi-
conproject(seehttp://wikipedia.org/wiki/Moby_Project). Itisalistof113,809official
crosswords;thatis,wordsthatareconsideredvalidincrosswordpuzzlesandotherword
games. In the Moby collection, the filename is 113809of.fic; you can download a copy,
withthesimplernamewords.txt,fromhttps://thinkpython.com/code/words.txt.
Thisfileisinplaintext,soyoucanopenitwithatexteditor,butyoucanalsoreaditfrom
Python. Thebuilt-infunctionopentakesthenameofthefileasaparameterandreturnsa
fileobjectyoucanusetoreadthefile.
>>> fin = open('words.txt')
fin is a common name for a file object used for input. The file object provides several
methodsforreading,includingreadline,whichreadscharactersfromthefileuntilitgets
toanewlineandreturnstheresultasastring:
>>> fin.readline()
'aa\n'
The first word in this particular list is “aa”, which is a kind of lava. The sequence \n
representsthenewlinecharacterthatseparatesthiswordfromthenext.
Thefileobjectkeepstrackofwhereitisinthefile, soifyoucallreadlineagain, youget
thenextword:
>>> fin.readline()
'aah\n'

84 Chapter9. Casestudy: wordplay
The next word is “aah”, which is a perfectly legitimate word, so stop looking at me like
that. Or, if it’s the newline character that’s bothering you, we can get rid of it with the
stringmethodstrip:
>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'
You can also use a file object as part of a for loop. This program reads words.txt and
printseachword,oneperline:
fin = open('words.txt')
for line in fin:
word = line.strip()
print(word)
9.2 Exercises
Therearesolutionstotheseexercisesinthenextsection. Youshouldatleastattempteach
onebeforeyoureadthesolutions.
Exercise9.1. Writeaprogramthatreadswords.txtandprintsonlythewordswithmorethan20
characters(notcountingwhitespace).
Exercise9.2. In1939ErnestVincentWrightpublisheda50,000wordnovelcalledGadsbythat
doesnotcontaintheletter“e”. Since“e”isthemostcommonletterinEnglish, that’snoteasyto
do.
Infact,itisdifficulttoconstructasolitarythoughtwithoutusingthatmostcommonsymbol. Itis
slowgoingatfirst,butwithcautionandhoursoftrainingyoucangraduallygainfacility.
Allright,I’llstopnow.
Writeafunctioncalledhas_no_ethatreturnsTrueifthegivenworddoesn’thavetheletter“e”in
it.
Writeaprogramthatreadswords.txtandprintsonlythewordsthathaveno“e”. Computethe
percentageofwordsinthelistthathaveno“e”.
Exercise9.3. Writeafunctionnamedavoidsthattakesawordandastringofforbiddenletters,
andthatreturnsTrueiftheworddoesn’tuseanyoftheforbiddenletters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
numberofwordsthatdon’tcontainanyofthem. Canyoufindacombinationof5forbiddenletters
thatexcludesthesmallestnumberofwords?
Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
thatreturnsTrueifthewordcontainsonlylettersinthelist. Canyoumakeasentenceusingonly
thelettersacefhlo? Otherthan“Hoealfalfa”?
Exercise9.5. Writeafunctionnameduses_allthattakesawordandastringofrequiredletters,
andthatreturnsTrueifthewordusesalltherequiredlettersatleastonce. Howmanywordsare
therethatuseallthevowelsaeiou? Howaboutaeiouy?
Exercise9.6. Writeafunctioncalledis_abecedarianthatreturnsTrueifthelettersinaword
appearinalphabeticalorder(doublelettersareok). Howmanyabecedarianwordsarethere?

9.3. Search 85
9.3 Search
Alloftheexercisesintheprevioussectionhavesomethingincommon;theycanbesolved
withthesearchpatternwesawinSection8.6. Thesimplestexampleis:
def has_no_e(word):
for letter in word:
if letter == 'e':
return False
return True
Theforlooptraversesthecharactersinword. Ifwefindtheletter“e”,wecanimmediately
returnFalse;otherwisewehavetogotothenextletter. Ifweexittheloopnormally,that
meanswedidn’tfindan“e”,sowereturnTrue.
Youcouldwritethisfunctionmoreconciselyusingtheinoperator,butIstartedwiththis
versionbecauseitdemonstratesthelogicofthesearchpattern.
avoidsisamoregeneralversionofhas_no_ebutithasthesamestructure:
def avoids(word, forbidden):
for letter in word:
if letter in forbidden:
return False
return True
WecanreturnFalseassoonaswefindaforbiddenletter;ifwegettotheendoftheloop,
wereturnTrue.
uses_onlyissimilarexceptthatthesenseoftheconditionisreversed:
def uses_only(word, available):
for letter in word:
if letter not in available:
return False
return True
Insteadofalistofforbiddenletters,wehavealistofavailableletters. Ifwefindaletterin
wordthatisnotinavailable,wecanreturnFalse.
uses_allissimilarexceptthatwereversetheroleofthewordandthestringofletters:
def uses_all(word, required):
for letter in required:
if letter not in word:
return False
return True
Insteadoftraversingthelettersinword,thelooptraversestherequiredletters. Ifanyofthe
requiredlettersdonotappearintheword,wecanreturnFalse.
If you were really thinking like a computer scientist, you would have recognized that
uses_allwasaninstanceofapreviouslysolvedproblem,andyouwouldhavewritten:
def uses_all(word, required):
return uses_only(required, word)
Thisisanexampleofaprogramdevelopmentplancalledreductiontoapreviouslysolved
problem,whichmeansthatyourecognizetheproblemyouareworkingonasaninstance
ofasolvedproblemandapplyanexistingsolution.

86 Chapter9. Casestudy: wordplay
9.4 Looping with indices
I wrote the functions in the previous section with for loops because I only needed the
charactersinthestrings;Ididn’thavetodoanythingwiththeindices.
Foris_abecedarianwehavetocompareadjacentletters,whichisalittletrickywithafor
loop:
def is_abecedarian(word):
previous = word[0]
for c in word:
if c < previous:
return False
previous = c
return True
Analternativeistouserecursion:
def is_abecedarian(word):
if len(word) <= 1:
return True
if word[0] > word[1]:
return False
return is_abecedarian(word[1:])
Anotheroptionistouseawhileloop:
def is_abecedarian(word):
i = 0
while i < len(word)-1:
if word[i+1] < word[i]:
return False
i = i+1
return True
Theloopstartsati=0andendswheni=len(word)-1. Eachtimethroughtheloop,itcom-
pares the ith character (which you can think of as the current character) to the i+1th
character(whichyoucanthinkofasthenext).
Ifthenextcharacterislessthan(alphabeticallybefore)thecurrentone,thenwehavedis-
coveredabreakintheabecedariantrend,andwereturnFalse.
Ifwegettotheendoftheloopwithoutfindingafault, thenthewordpassesthetest. To
convince yourself that the loop ends correctly, consider an example like 'flossy'. The
lengthofthewordis6,sothelasttimethelooprunsiswheniis4,whichistheindexof
thesecond-to-lastcharacter. Onthelastiteration,itcomparesthesecond-to-lastcharacter
tothelast,whichiswhatwewant.
Here is a version of is_palindrome (see Exercise 6.3) that uses two indices; one starts at
thebeginningandgoesup;theotherstartsattheendandgoesdown.
def is_palindrome(word):
i = 0
j = len(word)-1
while i<j:
if word[i] != word[j]:

9.5. Debugging 87
return False
i = i+1
j = j-1
return True
Orwecouldreducetoapreviouslysolvedproblemandwrite:
def is_palindrome(word):
return is_reverse(word, word)
Usingis_reversefromSection8.11.
9.5 Debugging
Testingprogramsishard. Thefunctionsinthischapterarerelativelyeasytotestbecause
youcanchecktheresultsbyhand. Evenso,itissomewherebetweendifficultandimpos-
sibletochooseasetofwordsthattestforallpossibleerrors.
Takinghas_no_easanexample,therearetwoobviouscasestocheck: wordsthathavean
‘e’ should return False, and words that don’t should return True. You should have no
troublecomingupwithoneofeach.
Within each case, there are some less obvious subcases. Among the words that have an
“e”, you should test words with an “e” at the beginning, the end, and somewhere in the
middle. You should test long words, short words, and very short words, like the empty
string. Theemptystringisanexampleofaspecialcase,whichisoneofthenon-obvious
caseswhereerrorsoftenlurk.
Inadditiontothetestcasesyougenerate,youcanalsotestyourprogramwithawordlist
likewords.txt. Byscanningtheoutput,youmightbeabletocatcherrors,butbecareful:
you might catch one kind of error (words that should not be included, but are) and not
another(wordsthatshouldbeincluded,butaren’t).
In general, testing can help you find bugs, but it is not easy to generate a good set of
test cases, and even if you do, you can’t be sure your program is correct. According to a
legendarycomputerscientist:
Programtestingcanbeusedtoshowthepresenceofbugs, butnevertoshow
theirabsence!
—EdsgerW.Dijkstra
9.6 Glossary
fileobject: Avaluethatrepresentsanopenfile.
reductiontoapreviouslysolvedproblem: A way of solving a problem by expressing it
asaninstanceofapreviouslysolvedproblem.
specialcase: Atestcasethatisatypicalornon-obvious(andlesslikelytobehandledcor-
rectly).

88 Chapter9. Casestudy: wordplay
9.7 Exercises
Exercise 9.7. This question is based on a Puzzler that was broadcast on the radio program Car
Talk(http://www.cartalk.com/content/puzzlers):
Give me a word with three consecutive double letters. I’ll give you a couple of words
thatalmostqualify,butdon’t. Forexample,thewordcommittee,c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
p-p-i. Ifyoucouldtakeoutthosei’sitwouldwork. Butthereisawordthathasthree
consecutivepairsoflettersandtothebestofmyknowledgethismaybetheonlyword.
Ofcoursethereareprobably500morebutIcanonlythinkofone. Whatistheword?
Writeaprogramtofindit. Solution: https://thinkpython.com/code/cartalk1.py.
Exercise 9.8. Here’s another Car Talk Puzzler (http://www.cartalk.com/content/
puzzlers):
“I was driving on the highway the other day and I happened to notice my odometer.
Likemostodometers,itshowssixdigits,inwholemilesonly. So,ifmycarhad300,000
miles,forexample,I’dsee3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits were
palindromic;thatis,theyreadthesameforwardasbackward. Forexample,5-4-4-5isa
palindrome,somyodometercouldhaveread3-1-5-4-4-5.
“Onemilelater,thelast5numberswerepalindromic. Forexample,itcouldhaveread
3-6-5-4-5-6. Onemileafterthat,themiddle4outof6numberswerepalindromic. And
youreadyforthis? Onemilelater,all6werepalindromic!
“Thequestionis,whatwasontheodometerwhenIfirstlooked?”
Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
theserequirements. Solution: https://thinkpython.com/code/cartalk2.py.
Exercise 9.9. Here’s another Car Talk Puzzler you can solve with a search (http://www.
cartalk.com/content/puzzlers):
“Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
wonderedhowoftenthishashappenedovertheyearsbutwegotsidetrackedwithother
topicsandwenevercameupwithananswer.
“WhenIgothomeIfiguredoutthatthedigitsofourageshavebeenreversiblesixtimes
sofar. Ialsofiguredoutthatifwe’reluckyitwouldhappenagaininafewyears,and
ifwe’rereallyluckyitwouldhappenonemoretimeafterthat. Inotherwords,itwould
havehappened8timesoverall. Sothequestionis,howoldamInow?”
WriteaPythonprogramthatsearchesforsolutionstothisPuzzler. Hint: youmightfindthestring
methodzfilluseful.
Solution: https://thinkpython.com/code/cartalk3.py.

| Chapter | 10  |     |     |     |
| ------- | --- | --- | --- | --- |
Lists
ThischapterpresentsoneofPython’smostusefulbuilt-intypes,lists. Youwillalsolearn
moreaboutobjectsandwhatcanhappenwhenyouhavemorethanonenameforthesame
object.
| 10.1 | A list is a | sequence |     |     |
| ---- | ----------- | -------- | --- | --- |
Likeastring, alistisasequenceofvalues. Inastring, thevaluesarecharacters; inalist,
theycanbeanytype. Thevaluesinalistarecalledelementsorsometimesitems.
Thereareseveralwaystocreateanewlist;thesimplestistoenclosetheelementsinsquare
brackets([and]):
| [10, 20,  | 30, 40]     |           |       |         |
| --------- | ----------- | --------- | ----- | ------- |
| ['crunchy | frog', 'ram | bladder', | 'lark | vomit'] |
Thefirstexampleisalistoffourintegers.Thesecondisalistofthreestrings.Theelements
of a list don’t have to be the same type. The following list contains a string, a float, an
| integer,and(lo!) | anotherlist: |      |     |     |
| ---------------- | ------------ | ---- | --- | --- |
| ['spam',         | 2.0, 5, [10, | 20]] |     |     |
Alistwithinanotherlistisnested.
A list that contains no elements is called an empty list; you can create one with empty
brackets,[].
Asyoumightexpect,youcanassignlistvaluestovariables:
| >>> cheeses        | = ['Cheddar', |          | 'Edam', 'Gouda'] |     |
| ------------------ | ------------- | -------- | ---------------- | --- |
| >>> numbers        | = [42,        | 123]     |                  |     |
| >>> empty          | = []          |          |                  |     |
| >>> print(cheeses, |               | numbers, | empty)           |     |
| ['Cheddar',        | 'Edam',       | 'Gouda'] | [42, 123]        | []  |

90 Chapter10. Lists
list
cheeses 0 ’Cheddar’
1 ’Edam’
2 ’Gouda’
list
numbers 0 42
1 123
5
list
empty
Figure10.1: Statediagram.
10.2 Lists are mutable
The syntax for accessing the elements of a list is the same as for accessing the characters
of a string—the bracket operator. The expression inside the brackets specifies the index.
Rememberthattheindicesstartat0:
>>> cheeses[0]
'Cheddar'
Unlikestrings,listsaremutable. Whenthebracketoperatorappearsontheleftsideofan
assignment,itidentifiestheelementofthelistthatwillbeassigned.
>>> numbers = [42, 123]
>>> numbers[1] = 5
>>> numbers
[42, 5]
Theone-ethelementofnumbers,whichusedtobe123,isnow5.
Figure10.1showsthestatediagramforcheeses,numbersandempty.
Lists are represented by boxes with the word “list” outside and the elements of the list
inside. cheeses refers to a list with three elements indexed 0, 1 and 2. numbers contains
twoelements;thediagramshowsthatthevalueofthesecondelementhasbeenreassigned
from123to5. emptyreferstoalistwithnoelements.
Listindicesworkthesamewayasstringindices:
• Anyintegerexpressioncanbeusedasanindex.
• Ifyoutrytoreadorwriteanelementthatdoesnotexist,yougetanIndexError.
• Ifanindexhasanegativevalue,itcountsbackwardfromtheendofthelist.
Theinoperatoralsoworksonlists.
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False

10.3. Traversingalist 91
| 10.3 | Traversing | a list |     |     |
| ---- | ---------- | ------ | --- | --- |
Themostcommonwaytotraversetheelementsofalistiswithaforloop.
Thesyntaxis
thesameasforstrings:
| for cheese | in cheeses: |     |     |     |
| ---------- | ----------- | --- | --- | --- |
print(cheese)
Thisworkswellifyouonlyneedtoreadtheelementsofthelist. Butifyouwanttowrite
orupdatetheelements,youneedtheindices. Acommonwaytodothatistocombinethe
built-infunctionsrangeandlen:
| for i in   | range(len(numbers)): |     |     |     |
| ---------- | -------------------- | --- | --- | --- |
| numbers[i] | = numbers[i]         | * 2 |     |     |
lenreturnsthenumberofelements
Thislooptraversesthelistandupdateseachelement.
inthelist. rangereturnsalistofindicesfrom0to n−1, where n isthelengthofthelist.
Eachtimethroughtheloopigetstheindexofthenextelement.
Theassignmentstatement
inthebodyusesitoreadtheoldvalueoftheelementandtoassignthenewvalue.
Aforloopoveranemptylistneverrunsthebody:
| for x in    | []:   |            |     |     |
| ----------- | ----- | ---------- | --- | --- |
| print('This | never | happens.') |     |     |
Althoughalistcancontainanotherlist,thenestedliststillcountsasasingleelement. The
lengthofthislistisfour:
| ['spam', | 1, ['Brie',     | 'Roquefort', | 'Pol le Veq'], | [1, 2, 3]] |
| -------- | --------------- | ------------ | -------------- | ---------- |
| 10.4     | List operations |              |                |            |
The+operatorconcatenateslists:
| >>> a = | [1, 2, 3] |     |     |     |
| ------- | --------- | --- | --- | --- |
| >>> b = | [4, 5, 6] |     |     |     |
| >>> c = | a + b     |     |     |     |
>>> c
| [1, 2, | 3, 4, 5, 6] |     |     |     |
| ------ | ----------- | --- | --- | --- |
The*operatorrepeatsalistagivennumberoftimes:
| >>> [0] | * 4         |          |     |     |
| ------- | ----------- | -------- | --- | --- |
| [0, 0,  | 0, 0]       |          |     |     |
| >>> [1, | 2, 3] * 3   |          |     |     |
| [1, 2,  | 3, 1, 2, 3, | 1, 2, 3] |     |     |
The first example repeats [0] four times. The second example repeats the list [1, 2, 3]
threetimes.
| 10.5 | List slices |     |     |     |
| ---- | ----------- | --- | --- | --- |
Thesliceoperatoralsoworksonlists:

| 92      |            |                |      | Chapter10. | Lists |
| ------- | ---------- | -------------- | ---- | ---------- | ----- |
| >>> t = | ['a', 'b', | 'c', 'd', 'e', | 'f'] |            |       |
>>> t[1:3]
['b', 'c']
>>> t[:4]
| ['a', 'b', | 'c', 'd'] |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |
>>> t[3:]
| ['d', 'e', | 'f'] |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- |
Ifyouomitthefirstindex,theslicestartsatthebeginning. Ifyouomitthesecond,theslice
| goestotheend. | Soifyouomitboth,thesliceisacopyofthewholelist. |     |     |     |     |
| ------------- | ---------------------------------------------- | --- | --- | --- | --- |
>>> t[:]
| ['a', 'b', | 'c', 'd', | 'e', 'f'] |     |     |     |
| ---------- | --------- | --------- | --- | --- | --- |
Sincelistsaremutable,itisoftenusefultomakeacopybeforeperformingoperationsthat
modifylists.
Asliceoperatorontheleftsideofanassignmentcanupdatemultipleelements:
| >>> t =    | ['a', 'b', | 'c', 'd', 'e', | 'f'] |     |     |
| ---------- | ---------- | -------------- | ---- | --- | --- |
| >>> t[1:3] | = ['x',    | 'y']           |      |     |     |
>>> t
| ['a', 'x', | 'y', 'd',    | 'e', 'f'] |     |     |     |
| ---------- | ------------ | --------- | --- | --- | --- |
| 10.6       | List methods |           |     |     |     |
Forexample,appendaddsanewelement
Pythonprovidesmethodsthatoperateonlists.
totheendofalist:
| >>> t = | ['a', 'b', | 'c'] |     |     |     |
| ------- | ---------- | ---- | --- | --- | --- |
>>> t.append('d')
>>> t
| ['a', 'b', | 'c', 'd'] |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |
extendtakesalistasanargumentandappendsalloftheelements:
| >>> t1 = | ['a', 'b', | 'c'] |     |     |     |
| -------- | ---------- | ---- | --- | --- | --- |
| >>> t2 = | ['d', 'e'] |      |     |     |     |
>>> t1.extend(t2)
>>> t1
| ['a', 'b', | 'c', 'd', | 'e'] |     |     |     |
| ---------- | --------- | ---- | --- | --- | --- |
Thisexampleleavest2unmodified.
sortarrangestheelementsofthelistfromlowtohigh:
| >>> t = | ['d', 'c', | 'e', 'b', 'a'] |     |     |     |
| ------- | ---------- | -------------- | --- | --- | --- |
>>> t.sort()
>>> t
| ['a', 'b', | 'c', 'd', | 'e'] |     |     |     |
| ---------- | --------- | ---- | --- | --- | --- |
Mostlistmethodsarevoid;theymodifythelistandreturnNone.
Ifyouaccidentallywrite
t = t.sort(),youwillbedisappointedwiththeresult.

10.7. Map,filterandreduce 93
| 10.7 Map, | filter and | reduce |
| --------- | ---------- | ------ |
Toaddupallthenumbersinalist,youcanusealooplikethis:
def add_all(t):
| total =  | 0   |     |
| -------- | --- | --- |
| for x in | t:  |     |
total += x
| return | total |     |
| ------ | ----- | --- |
total is initialized to 0. Each time through the loop, x gets one element from the list.
+=
The operator provides a short way to update a variable. This augmented assignment
statement,
| total += | x   |     |
| -------- | --- | --- |
isequivalentto
| total = | total + x |     |
| ------- | --------- | --- |
Astheloopruns,totalaccumulatesthesumoftheelements;
avariableusedthiswayis
sometimescalledanaccumulator.
AddinguptheelementsofalistissuchacommonoperationthatPythonprovidesitasa
built-infunction,sum:
| >>> t = [1, | 2, 3] |     |
| ----------- | ----- | --- |
>>> sum(t)
6
An operation like this that combines a sequence of elements into a single value is some-
timescalledreduce.
Sometimesyouwanttotraverseonelistwhilebuildinganother.Forexample,thefollowing
functiontakesalistofstringsandreturnsanewlistthatcontainscapitalizedstrings:
def capitalize_all(t):
| res = [] |     |     |
| -------- | --- | --- |
| for s in | t:  |     |
res.append(s.capitalize())
| return | res |     |
| ------ | --- | --- |
resisinitializedwithanemptylist; eachtimethroughtheloop, weappendthenextele-
Soresisanotherkindofaccumulator.
ment.
Anoperationlikecapitalize_allissometimescalledamapbecauseit“maps”afunction
(inthiscasethemethodcapitalize)ontoeachoftheelementsinasequence.
Anothercommonoperationistoselectsomeoftheelementsfromalistandreturnasublist.
For example, the following function takes a list of strings and returns a list that contains
onlytheuppercasestrings:
def only_upper(t):
| res = [] |     |     |
| -------- | --- | --- |
| for s in | t:  |     |
if s.isupper():
res.append(s)
| return | res |     |
| ------ | --- | --- |

| 94  |     |     |     | Chapter10. | Lists |
| --- | --- | --- | --- | ---------- | ----- |
isupperisastringmethodthatreturnsTrueifthestringcontainsonlyuppercaseletters.
Anoperationlikeonly_upperiscalledafilterbecauseitselectssomeoftheelementsand
filtersouttheothers.
Mostcommonlistoperationscanbeexpressedasacombinationofmap,filterandreduce.
| 10.8 Deleting | elements |     |     |     |     |
| ------------- | -------- | --- | --- | --- | --- |
Thereareseveralwaystodeleteelementsfromalist. Ifyouknowtheindexoftheelement
youwant,youcanusepop:
| >>> t = ['a',    | 'b', 'c'] |     |     |     |     |
| ---------------- | --------- | --- | --- | --- | --- |
| >>> x = t.pop(1) |           |     |     |     |     |
>>> t
['a', 'c']
>>> x
'b'
pop
modifies the list and returns the element that was removed. If you don’t provide an
index,itdeletesandreturnsthelastelement.
Ifyoudon’tneedtheremovedvalue,youcanusethedeloperator:
| >>> t = ['a', | 'b', 'c'] |     |     |     |     |
| ------------- | --------- | --- | --- | --- | --- |
| >>> del t[1]  |           |     |     |     |     |
>>> t
['a', 'c']
Ifyouknowtheelementyouwanttoremove(butnottheindex),youcanuseremove:
| >>> t = ['a', | 'b', 'c'] |     |     |     |     |
| ------------- | --------- | --- | --- | --- | --- |
>>> t.remove('b')
>>> t
['a', 'c']
ThereturnvaluefromremoveisNone.
Toremovemorethanoneelement,youcanusedelwithasliceindex:
| >>> t = ['a',  | 'b', 'c', | 'd', 'e', | 'f'] |     |     |
| -------------- | --------- | --------- | ---- | --- | --- |
| >>> del t[1:5] |           |           |      |     |     |
>>> t
['a', 'f']
Asusual,thesliceselectsalltheelementsuptobutnotincludingthesecondindex.
| 10.9 Lists | and strings |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
Astringisasequenceofcharactersandalistisasequenceofvalues,butalistofcharacters
isnotthesameasastring. Toconvertfromastringtoalistofcharacters,youcanuselist:
| >>> s = 'spam'  |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
| >>> t = list(s) |     |     |     |     |     |
>>> t
| ['s', 'p', | 'a', 'm'] |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |

10.10. Objectsandvalues 95
a ’banana’ a
’banana’
b ’banana’ b
Figure10.2: Statediagram.
list
Because is the name of a built-in function, you should avoid using it as a variable
name. Ialsoavoidlbecauseitlookstoomuchlike1. Sothat’swhyIuset.
Thelistfunctionbreaksastringintoindividualletters. Ifyouwanttobreakastringinto
words,youcanusethesplitmethod:
| >>> s = | 'pining for the | fjords' |
| ------- | --------------- | ------- |
| >>> t = | s.split()       |         |
>>> t
| ['pining', | 'for', 'the', | 'fjords'] |
| ---------- | ------------- | --------- |
Anoptionalargumentcalledadelimiterspecifieswhichcharacterstouseaswordbound-
aries. Thefollowingexampleusesahyphenasadelimiter:
| >>> s =       | 'spam-spam-spam'   |     |
| ------------- | ------------------ | --- |
| >>> delimiter | = '-'              |     |
| >>> t =       | s.split(delimiter) |     |
>>> t
| ['spam', | 'spam', 'spam'] |     |
| -------- | --------------- | --- |
joinistheinverseofsplit. joinis
Ittakesalistofstringsandconcatenatestheelements.
astringmethod,soyouhavetoinvokeitonthedelimiterandpassthelistasaparameter:
| >>> t =       | ['pining', 'for', | 'the', 'fjords'] |
| ------------- | ----------------- | ---------------- |
| >>> delimiter | = ' '             |                  |
| >>> s =       | delimiter.join(t) |                  |
>>> s
| 'pining | for the fjords' |     |
| ------- | --------------- | --- |
In this case the delimiter is a space character, so join puts a space between words. To
concatenatestringswithoutspaces,youcanusetheemptystring,'',asadelimiter.
| 10.10 | Objects and | values |
| ----- | ----------- | ------ |
Ifweruntheseassignmentstatements:
a = 'banana'
b = 'banana'
Weknowthataandbbothrefertoastring,butwedon’tknowwhethertheyrefertothe
| samestring. | Therearetwopossiblestates,showninFigure10.2. |     |
| ----------- | -------------------------------------------- | --- |
Inonecase,aandbrefertotwodifferentobjectsthathavethesamevalue. Inthesecond
case,theyrefertothesameobject.
Tocheckwhethertwovariablesrefertothesameobject,youcanusetheisoperator.

96 Chapter10. Lists
a [ 1, 2, 3 ]
b [ 1, 2, 3 ]
Figure10.3: Statediagram.
a
[ 1, 2, 3 ]
b
Figure10.4: Statediagram.
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
In this example, Python only created one string object, and both a and b refer to it. But
whenyoucreatetwolists,yougettwoobjects:
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
SothestatediagramlookslikeFigure10.3.
Inthiscasewewouldsaythatthetwolistsareequivalent,becausetheyhavethesameel-
ements,butnotidentical,becausetheyarenotthesameobject. Iftwoobjectsareidentical,
theyarealsoequivalent,butiftheyareequivalent,theyarenotnecessarilyidentical.
Untilnow,wehavebeenusing“object”and“value”interchangeably,butitismoreprecise
to say that an object has a value. If you evaluate [1, 2, 3], you get a list object whose
value is a sequence of integers. If another list has the same elements, we say it has the
samevalue,butitisnotthesameobject.
10.11 Aliasing
Ifareferstoanobjectandyouassignb = a,thenbothvariablesrefertothesameobject:
>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
ThestatediagramlookslikeFigure10.4.
Theassociationofavariablewithanobjectiscalledareference. Inthisexample,thereare
tworeferencestothesameobject.
Anobjectwithmorethanonereferencehasmorethanonename,sowesaythattheobject
isaliased.
Ifthealiasedobjectismutable,changesmadewithonealiasaffecttheother:

10.12. Listarguments 97
list
__main__ letters
0 ’a’
1 ’b’
delete_head t
2 ’c’
Figure10.5: Stackdiagram.
>>> b[0] = 42
>>> a
[42, 2, 3]
Although this behavior can be useful, it is error-prone. In general, it is safer to avoid
aliasingwhenyouareworkingwithmutableobjects.
Forimmutableobjectslikestrings,aliasingisnotasmuchofaproblem. Inthisexample:
a = 'banana'
b = 'banana'
Italmostnevermakesadifferencewhetheraandbrefertothesamestringornot.
10.12 List arguments
Whenyoupassalisttoafunction,thefunctiongetsareferencetothelist. Ifthefunction
modifies the list, the caller sees the change. For example, delete_head removes the first
elementfromalist:
def delete_head(t):
del t[0]
Here’showitisused:
>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
>>> letters
['b', 'c']
Theparametertandthevariablelettersarealiasesforthesameobject.Thestackdiagram
lookslikeFigure10.5.
Sincethelistissharedbytwoframes,Idrewitbetweenthem.
Itisimportanttodistinguishbetweenoperationsthatmodifylistsandoperationsthatcre-
atenewlists. Forexample,theappendmethodmodifiesalist,butthe+operatorcreatesa
newlist.
Here’sanexampleusingappend:
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> t1
[1, 2, 3]
>>> t2
None

| 98  |     |     | Chapter10. | Lists |
| --- | --- | --- | ---------- | ----- |
ThereturnvaluefromappendisNone.
Here’sanexampleusingthe+operator:
| >>> t3 = | t1 + [4] |     |     |     |
| -------- | -------- | --- | --- | --- |
>>> t1
[1, 2, 3]
>>> t3
| [1, 2, 3, | 4]  |     |     |     |
| --------- | --- | --- | --- | --- |
Theresultoftheoperatorisanewlist,andtheoriginallistisunchanged.
This difference is important when you write functions that are supposed to modify lists.
Forexample,thisfunctiondoesnotdeletetheheadofalist:
def bad_delete_head(t):
| t = t[1:] |     | # WRONG! |     |     |
| --------- | --- | -------- | --- | --- |
Thesliceoperatorcreatesanewlistandtheassignmentmakestrefertoit,butthatdoesn’t
affectthecaller.
| >>> t4 = | [1, 2, 3] |     |     |     |
| -------- | --------- | --- | --- | --- |
>>> bad_delete_head(t4)
>>> t4
[1, 2, 3]
Atthebeginningofbad_delete_head,tandt4refertothesamelist. Attheend,trefers
toanewlist,butt4stillreferstotheoriginal,unmodifiedlist.
Analternativeistowriteafunctionthatcreatesandreturnsanewlist. Forexample,tail
returnsallbutthefirstelementofalist:
def tail(t):
| return | t[1:] |     |     |     |
| ------ | ----- | --- | --- | --- |
Thisfunctionleavestheoriginallistunmodified. Here’showitisused:
| >>> letters | = ['a', 'b',    | 'c'] |     |     |
| ----------- | --------------- | ---- | --- | --- |
| >>> rest    | = tail(letters) |      |     |     |
>>> rest
['b', 'c']
| 10.13 | Debugging |     |     |     |
| ----- | --------- | --- | --- | --- |
Carelessuseoflists(andothermutableobjects)canleadtolonghoursofdebugging. Here
aresomecommonpitfallsandwaystoavoidthem:
1. MostlistmethodsmodifytheargumentandreturnNone. Thisistheoppositeofthe
stringmethods,whichreturnanewstringandleavetheoriginalalone.
Ifyouareusedtowritingstringcodelikethis:
| word | = word.strip() |     |     |     |
| ---- | -------------- | --- | --- | --- |
Itistemptingtowritelistcodelikethis:

10.13. Debugging 99
t = t.sort() # WRONG!
BecausesortreturnsNone,thenextoperationyouperformwithtislikelytofail.
Before using list methods and operators, you should read the documentation care-
fullyandthentestthemininteractivemode.
2. Pickanidiomandstickwithit.
Partoftheproblemwithlistsisthattherearetoomanywaystodothings. Forexam-
ple, to remove an element from a list, you can use pop, remove, del, or even a slice
assignment.
Toaddanelement,youcanusetheappendmethodorthe+operator. Assumingthat
tisalistandxisalistelement,thesearecorrect:
t.append(x)
t = t + [x]
t += [x]
Andthesearewrong:
t.append([x]) # WRONG!
t = t.append(x) # WRONG!
t + [x] # WRONG!
t = t + x # WRONG!
Try out each of these examples in interactive mode to make sure you understand
whattheydo. Noticethatonlythelastonecausesaruntimeerror;theotherthreeare
legal,buttheydothewrongthing.
3. Makecopiestoavoidaliasing.
If you want to use a method like sort that modifies the argument, but you need to
keeptheoriginallistaswell,youcanmakeacopy.
>>> t = [3, 1, 2]
>>> t2 = t[:]
>>> t2.sort()
>>> t
[3, 1, 2]
>>> t2
[1, 2, 3]
Inthisexampleyoucouldalsousethebuilt-infunctionsorted,whichreturnsanew,
sortedlistandleavestheoriginalalone.
>>> t2 = sorted(t)
>>> t
[3, 1, 2]
>>> t2
[1, 2, 3]

| 100            |     |     |     | Chapter10. | Lists |
| -------------- | --- | --- | --- | ---------- | ----- |
| 10.14 Glossary |     |     |     |            |       |
list: Asequenceofvalues.
| element: Oneofthevaluesinalist(orothersequence),alsocalleditems. |                                                 |     |     |     |     |
| ---------------------------------------------------------------- | ----------------------------------------------- | --- | --- | --- | --- |
| nestedlist:                                                      | Alistthatisanelementofanotherlist.              |     |     |     |     |
| accumulator:                                                     | Avariableusedinalooptoadduporaccumulatearesult. |     |     |     |     |
augmentedassignment: Astatementthatupdatesthevalueofavariableusinganopera-
torlike+=.
reduce: Aprocessingpatternthattraversesasequenceandaccumulatestheelementsinto
asingleresult.
map: A processing pattern that traverses a sequence and performs an operation on each
element.
filter: Aprocessingpatternthattraversesalistandselectstheelementsthatsatisfysome
criterion.
| object: Somethingavariablecanreferto.                   |                                            | Anobjecthasatypeandavalue. |     |     |     |
| ------------------------------------------------------- | ------------------------------------------ | -------------------------- | --- | --- | --- |
| equivalent:                                             | Havingthesamevalue.                        |                            |     |     |     |
| identical: Beingthesameobject(whichimpliesequivalence). |                                            |                            |     |     |     |
| reference:                                              | Theassociationbetweenavariableanditsvalue. |                            |     |     |     |
aliasing: Acircumstancewheretwoormorevariablesrefertothesameobject.
delimiter: Acharacterorstringusedtoindicatewhereastringshouldbesplit.
| 10.15 Exercises |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
https://thinkpython.com/code/
| You can download | solutions | to these exercises | from |     |     |
| ---------------- | --------- | ------------------ | ---- | --- | --- |
list_exercises.py.
Writeafunctioncallednested_sumthattakesalistoflistsofintegersandaddsup
Exercise10.1.
| theelementsfromallofthenestedlists. |              | Forexample: |     |     |     |
| ----------------------------------- | ------------ | ----------- | --- | --- | --- |
| >>> t = [[1,                        | 2], [3], [4, | 5, 6]]      |     |     |     |
>>> nested_sum(t)
21
Exercise10.2. Writeafunctioncalledcumsumthattakesalistofnumbersandreturnsthecumu-
lativesum; thatis, anewlistwherethe ithelementisthesumofthefirst i+1elementsfromthe
| originallist. | Forexample: |     |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- |
| >>> t = [1,   | 2, 3]       |     |     |     |     |
>>> cumsum(t)
[1, 3, 6]
Writeafunctioncalledmiddlethattakesalistandreturnsanewlistthatcontains
Exercise10.3.
| allbutthefirstandlastelements. |          | Forexample: |     |     |     |
| ------------------------------ | -------- | ----------- | --- | --- | --- |
| >>> t = [1,                    | 2, 3, 4] |             |     |     |     |
>>> middle(t)
[2, 3]

10.15. Exercises 101
Exercise10.4. Writeafunctioncalledchopthattakesalist,modifiesitbyremovingthefirstand
lastelements,andreturnsNone. Forexample:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
Exercise10.5. Writeafunctioncalledis_sortedthattakesalistasaparameterandreturnsTrue
ifthelistissortedinascendingorderandFalseotherwise. Forexample:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
Exercise10.6. Twowordsareanagramsifyoucanrearrangethelettersfromonetospelltheother.
Writeafunctioncalledis_anagramthattakestwostringsandreturnsTrueiftheyareanagrams.
Exercise10.7. Writeafunctioncalledhas_duplicatesthattakesalistandreturnsTrueifthere
isanyelementthatappearsmorethanonce. Itshouldnotmodifytheoriginallist.
Exercise10.8. Thisexercisepertainstotheso-calledBirthdayParadox,whichyoucanreadabout
athttp://en.wikipedia.org/wiki/Birthday_paradox.
Ifthereare23studentsinyourclass,whatarethechancesthattwoofthemhavethesamebirthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.
Youcandownloadmysolutionfromhttps://thinkpython.com/code/birthday.py.
Exercise10.9. Writeafunctionthatreadsthefilewords.txtandbuildsalistwithoneelement
per word. Write two versions of this function, one using the append method and the other using
theidiomt = t + [x]. Whichonetakeslongertorun? Why?
Solution: https://thinkpython.com/code/wordlist.py.
Exercise10.10. Tocheckwhetherawordisinthewordlist,youcouldusetheinoperator,butit
wouldbeslowbecauseitsearchesthroughthewordsinorder.
Because the words are in alphabetical order, we can speed things up with a bisection search (also
knownasbinarysearch),whichissimilartowhatyoudowhenyoulookawordupinthedictionary
(thebook,notthedatastructure). Youstartinthemiddleandchecktoseewhetherthewordyouare
lookingforcomesbeforethewordinthemiddleofthelist. Ifso,yousearchthefirsthalfofthelist
thesameway. Otherwiseyousearchthesecondhalf.
Eitherway,youcuttheremainingsearchspaceinhalf. Ifthewordlisthas113,809words,itwill
takeabout17stepstofindthewordorconcludethatit’snotthere.
Write a function called in_bisect that takes a sorted list and a target value and returns True if
thewordisinthelistandFalseifit’snot.
Or you could read the documentation of the bisect module and use that! Solution: https:
//thinkpython.com/code/inlist.py.
Exercise10.11. Twowordsarea“reversepair”ifeachisthereverseoftheother. Writeaprogram
that finds all the reverse pairs in the word list. Solution: https://thinkpython.com/code/
reverse_pair.py.
Exercise 10.12. Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled”. Solution: https://

102 Chapter10. Lists
thinkpython.com/code/interlock.py. Credit: This exercise is inspired by an example at
http://puzzlers.org.
1. Writeaprogramthatfindsallpairsofwordsthatinterlock. Hint: don’tenumerateallpairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
word,startingfromthefirst,secondorthird?

Chapter 11
Dictionaries
This chapter presents another built-in type called a dictionary. Dictionaries are one of
Python’s best features; they are the building blocks of many efficient and elegant algo-
rithms.
11.1 A dictionary is a mapping
Adictionaryislikealist, butmoregeneral. Inalist, theindiceshavetobeintegers; ina
dictionarytheycanbe(almost)anytype.
A dictionary contains a collection of indices, which are called keys, and a collection of
values. Eachkeyisassociatedwithasinglevalue. Theassociationofakeyandavalueis
calledakey-valuepairorsometimesanitem.
Inmathematicallanguage,adictionaryrepresentsamappingfromkeystovalues,soyou
canalsosaythateachkey“mapsto”avalue. Asanexample,we’llbuildadictionarythat
mapsfromEnglishtoSpanishwords,sothekeysandthevaluesareallstrings.
Thefunctiondictcreatesanewdictionarywithnoitems. Becausedictisthenameofa
built-infunction,youshouldavoidusingitasavariablename.
>>> eng2sp = dict()
>>> eng2sp
{}
The squiggly-brackets, {}, represent an empty dictionary. To add items to the dictionary,
youcanusesquarebrackets:
>>> eng2sp['one'] = 'uno'
Thislinecreatesanitemthatmapsfromthekey'one'tothevalue'uno'. Ifweprintthe
dictionaryagain,weseeakey-valuepairwithacolonbetweenthekeyandvalue:
>>> eng2sp
{'one': 'uno'}
Thisoutputformatisalsoaninputformat. Forexample,youcancreateanewdictionary
withthreeitems:

| 104        |           |               |                 | Chapter11. | Dictionaries |
| ---------- | --------- | ------------- | --------------- | ---------- | ------------ |
| >>> eng2sp | = {'one': | 'uno', 'two': | 'dos', 'three': | 'tres'}    |              |
Butifyouprinteng2sp,youmightbesurprised:
>>> eng2sp
| {'one': | 'uno', 'three': | 'tres', | 'two': 'dos'} |     |     |
| ------- | --------------- | ------- | ------------- | --- | --- |
The order of the key-value pairs might not be the same. If you type the same example
on your computer, you might get a different result. In general, the order of items in a
dictionaryisunpredictable.
Butthat’snotaproblembecausetheelementsofadictionaryareneverindexedwithinte-
| gerindices. | Instead,youusethekeystolookupthecorrespondingvalues: |     |     |     |     |
| ----------- | ---------------------------------------------------- | --- | --- | --- | --- |
>>> eng2sp['two']
'dos'
Thekey'two'alwaysmapstothevalue'dos'sotheorderoftheitemsdoesn’tmatter.
Ifthekeyisn’tinthedictionary,yougetanexception:
>>> eng2sp['four']
| KeyError: | 'four' |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
Thelenfunctionworksondictionaries;itreturnsthenumberofkey-valuepairs:
>>> len(eng2sp)
3
Theinoperatorworksondictionaries,too;ittellsyouwhethersomethingappearsasakey
inthedictionary(appearingasavalueisnotgoodenough).
| >>> 'one' | in eng2sp |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- |
True
| >>> 'uno' | in eng2sp |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- |
False
To see whether something appears as a value in a dictionary, you can use the method
values,whichreturnsacollectionofvalues,andthenusetheinoperator:
| >>> vals  | = eng2sp.values() |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- |
| >>> 'uno' | in vals           |     |     |     |     |
True
Theinoperatorusesdifferentalgorithmsforlistsanddictionaries. Forlists,itsearchesthe
elementsofthelistinorder, asinSection8.6. Asthelistgetslonger, thesearchtimegets
longerindirectproportion.
Pythondictionariesuseadatastructurecalledahashtablethathasaremarkableproperty:
theinoperatortakesaboutthesameamountoftimenomatterhowmanyitemsareinthe
dictionary.Iexplainhowthat’spossibleinSectionB.4,buttheexplanationmightnotmake
senseuntilyou’vereadafewmorechapters.
| 11.2 | Dictionary | as a collection | of counters |     |     |
| ---- | ---------- | --------------- | ----------- | --- | --- |
Supposeyouaregivenastringandyouwanttocounthowmanytimeseachletterappears.
Thereareseveralwaysyoucoulddoit:

11.2. Dictionaryasacollectionofcounters 105
1. Youcouldcreate26variables,oneforeachletterofthealphabet. Thenyoucouldtra-
versethestringand,foreachcharacter,incrementthecorrespondingcounter,proba-
blyusingachainedconditional.
2. You could create a list with 26 elements. Then you could convert each character to
anumber(usingthebuilt-infunctionord),usethenumberasanindexintothelist,
andincrementtheappropriatecounter.
3. Youcouldcreateadictionarywithcharactersaskeysandcountersasthecorrespond-
ingvalues.Thefirsttimeyouseeacharacter,youwouldaddanitemtothedictionary.
Afterthatyouwouldincrementthevalueofanexistingitem.
Eachoftheseoptionsperformsthesamecomputation, buteachofthemimplementsthat
computationinadifferentway.
An implementation is a way of performing a computation; some implementations are
betterthanothers. Forexample,anadvantageofthedictionaryimplementationisthatwe
don’thavetoknowaheadoftimewhichlettersappearinthestringandweonlyhaveto
makeroomforthelettersthatdoappear.
Hereiswhatthecodemightlooklike:
def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
else:
d[c] += 1
return d
Thenameofthefunctionishistogram,whichisastatisticaltermforacollectionofcounters
(orfrequencies).
Thefirstlineofthefunctioncreatesanemptydictionary. Theforlooptraversesthestring.
Eachtimethroughtheloop,ifthecharactercisnotinthedictionary,wecreateanewitem
withkeycandtheinitialvalue1(sincewehaveseenthisletteronce). Ifcisalreadyinthe
dictionaryweincrementd[c].
Here’showitworks:
>>> h = histogram('brontosaurus')
>>> h
{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
Thehistogramindicatesthattheletters'a'and'b'appearonce; 'o'appearstwice, and
soon.
Dictionaries have a method called get that takes a key and a default value. If the key
appears in the dictionary, get returns the corresponding value; otherwise it returns the
defaultvalue. Forexample:
>>> h = histogram('a')
>>> h
{'a': 1}
>>> h.get('a', 0)

106 Chapter11. Dictionaries
1
>>> h.get('c', 0)
0
Asanexercise,usegettowritehistogrammoreconcisely. Youshouldbeabletoeliminate
theifstatement.
11.3 Looping and dictionaries
Ifyouuseadictionaryinaforstatement,ittraversesthekeysofthedictionary. Forexam-
ple,print_histprintseachkeyandthecorrespondingvalue:
def print_hist(h):
for c in h:
print(c, h[c])
Here’swhattheoutputlookslike:
>>> h = histogram('parrot')
>>> print_hist(h)
a 1
p 1
r 2
t 1
o 1
Again,thekeysareinnoparticularorder. Totraversethekeysinsortedorder,youcanuse
thebuilt-infunctionsorted:
>>> for key in sorted(h):
... print(key, h[key])
a 1
o 1
p 1
r 2
t 1
11.4 Reverse lookup
Givenadictionarydandakeyk,itiseasytofindthecorrespondingvaluev = d[k]. This
operationiscalledalookup.
Butwhatifyouhavevandyouwanttofindk? Youhavetwoproblems: first,theremight
bemorethanonekeythatmapstothevaluev. Dependingontheapplication,youmight
be able to pick one, or you might have to make a list that contains all of them. Second,
thereisnosimplesyntaxtodoareverselookup;youhavetosearch.
Hereisafunctionthattakesavalueandreturnsthefirstkeythatmapstothatvalue:
def reverse_lookup(d, v):
for k in d:
if d[k] == v:
return k
raise LookupError()

11.5. Dictionariesandlists 107
Thisfunctionisyetanotherexampleofthesearchpattern,butitusesafeaturewehaven’t
seen before, raise. The raise statement causes an exception; in this case it causes a
LookupError,whichisabuilt-inexceptionusedtoindicatethatalookupoperationfailed.
Ifwegettotheendoftheloop,thatmeansvdoesn’tappearinthedictionaryasavalue,so
weraiseanexception.
Hereisanexampleofasuccessfulreverselookup:
| >>> h = | histogram('parrot') |     |     |     |     |
| ------- | ------------------- | --- | --- | --- | --- |
| >>> key | = reverse_lookup(h, |     | 2)  |     |     |
>>> key
'r'
Andanunsuccessfulone:
| >>> key   | = reverse_lookup(h, |        | 3)                   |     |     |
| --------- | ------------------- | ------ | -------------------- | --- | --- |
| Traceback | (most               | recent | call last):          |     |     |
| File      | "<stdin>",          | line   | 1, in <module>       |     |     |
| File      | "<stdin>",          | line   | 5, in reverse_lookup |     |     |
LookupError
TheeffectwhenyouraiseanexceptionisthesameaswhenPythonraisesone: itprintsa
tracebackandanerrormessage.
When you raise an exception, you can provide a detailed error message as an optional
| argument.    | Forexample:        |        |             |            |                     |
| ------------ | ------------------ | ------ | ----------- | ---------- | ------------------- |
| >>> raise    | LookupError('value |        | does        | not appear | in the dictionary') |
| Traceback    | (most              | recent | call last): |            |                     |
| File         | "<stdin>",         | line   | 1, in ?     |            |                     |
| LookupError: | value              | does   | not appear  | in the     | dictionary          |
Areverselookupismuchslowerthanaforwardlookup;ifyouhavetodoitoften,orifthe
dictionarygetsbig,theperformanceofyourprogramwillsuffer.
| 11.5 | Dictionaries |     | and lists |     |     |
| ---- | ------------ | --- | --------- | --- | --- |
Listscanappearasvaluesinadictionary. Forexample,ifyouaregivenadictionarythat
maps from letters to frequencies, you might want to invert it; that is, create a dictionary
that maps from frequencies to letters. Since there might be several letters with the same
frequency,eachvalueintheinverteddictionaryshouldbealistofletters.
Hereisafunctionthatinvertsadictionary:
def invert_dict(d):
| inverse | = dict() |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- |
| for     | key in   | d:  |     |     |     |
val = d[key]
|     | if val       | not in | inverse: |     |     |
| --- | ------------ | ------ | -------- | --- | --- |
|     | inverse[val] |        | = [key]  |     |     |
else:
inverse[val].append(key)
| return | inverse |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- |

| 108 |      |      |       |           | Chapter11. | Dictionaries |
| --- | ---- | ---- | ----- | --------- | ---------- | ------------ |
|     |      | dict |       | dict list |            |              |
|     | hist |      | ’a’ 1 | inv 1     | 0 ’a’      |              |
|     |      |      | ’p’ 1 |           | 1 ’p’      |              |
|     |      |      | ’r’ 2 |           | 2 ’t’      |              |
|     |      |      | ’t’ 1 |           | 3 ’o’      |              |
|     |      |      | ’o’ 1 |           |            |              |
list
|     |     |     |             | 2             | 0 ’r’ |     |
| --- | --- | --- | ----------- | ------------- | ----- | --- |
|     |     |     | Figure11.1: | Statediagram. |       |     |
Eachtimethroughtheloop, keygetsakeyfromdandvalgetsthecorrespondingvalue.
Ifvalisnotininverse,thatmeanswehaven’tseenitbefore,sowecreateanewitemand
initializeitwithasingleton(alistthatcontainsasingleelement). Otherwisewehaveseen
thisvaluebefore,soweappendthecorrespondingkeytothelist.
Hereisanexample:
| >>> hist | = histogram('parrot') |     |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- | --- |
>>> hist
| {'a': 1,    | 'p': 1,             | 'r': | 2, 't': 1, 'o': | 1}  |     |     |
| ----------- | ------------------- | ---- | --------------- | --- | --- | --- |
| >>> inverse | = invert_dict(hist) |      |                 |     |     |     |
>>> inverse
| {1: ['a', | 'p', | 't', 'o'], | 2: ['r']} |     |     |     |
| --------- | ---- | ---------- | --------- | --- | --- | --- |
Figure11.1isastatediagramshowinghistandinverse.
Adictionaryisrepresentedasa
boxwiththetypedictaboveitandthekey-valuepairsinside. Ifthevaluesareintegers,
floatsorstrings,Idrawtheminsidethebox,butIusuallydrawlistsoutsidethebox,just
tokeepthediagramsimple.
Listscanbevaluesinadictionary,asthisexampleshows,buttheycannotbekeys. Here’s
whathappensifyoutry:
| >>> t =    | [1, 2,     | 3]      |                |     |     |     |
| ---------- | ---------- | ------- | -------------- | --- | --- | --- |
| >>> d =    | dict()     |         |                |     |     |     |
| >>> d[t]   | = 'oops'   |         |                |     |     |     |
| Traceback  | (most      | recent  | call last):    |     |     |     |
| File       | "<stdin>", | line    | 1, in ?        |     |     |     |
| TypeError: | list       | objects | are unhashable |     |     |     |
Imentionedearlierthatadictionaryisimplementedusingahashtableandthatmeansthat
thekeyshavetobehashable.
A hash is a function that takes a value (of any kind) and returns an integer. Dictionaries
usetheseintegers,calledhashvalues,tostoreandlookupkey-valuepairs.
This system works fine if the keys are immutable. But if the keys are mutable, like lists,
badthingshappen. Forexample,whenyoucreateakey-valuepair,Pythonhashesthekey
andstoresitinthecorrespondinglocation. Ifyoumodifythekeyandthenhashitagain,it
wouldgotoadifferentlocation. Inthatcaseyoumighthavetwoentriesforthesamekey,
oryoumightnotbeabletofindakey. Eitherway,thedictionarywouldn’tworkcorrectly.
That’swhykeyshavetobehashable,andwhymutabletypeslikelistsaren’t. Thesimplest
waytogetaroundthislimitationistousetuples,whichwewillseeinthenextchapter.

11.6. Memos 109
fibonacci
n 4
fibonacci fibonacci
n 3 n 2
fibonacci fibonacci fibonacci fibonacci
n 2 n 1 n 1 n 0
fibonacci fibonacci
n 1 n 0
Figure11.2: Callgraph.
Sincedictionariesaremutable,theycan’tbeusedaskeys,buttheycanbeusedasvalues.
11.6 Memos
IfyouplayedwiththefibonaccifunctionfromSection6.7, youmighthavenoticedthat
the bigger the argument you provide, the longer the function takes to run. Furthermore,
theruntimeincreasesquickly.
Tounderstandwhy,considerFigure11.2,whichshowsthecallgraphforfibonacciwith
n=4:
Acallgraphshowsasetoffunctionframes,withlinesconnectingeachframetotheframes
ofthefunctionsitcalls. Atthetopofthegraph,fibonacciwithn=4callsfibonacciwith
n=3andn=2. Inturn,fibonacciwithn=3callsfibonacciwithn=2andn=1. Andsoon.
Counthowmanytimesfibonacci(0)andfibonacci(1)arecalled. Thisisaninefficient
solutiontotheproblem,anditgetsworseastheargumentgetsbigger.
Onesolutionistokeeptrackofvaluesthathavealreadybeencomputedbystoringthem
inadictionary. Apreviouslycomputedvaluethatisstoredforlateruseiscalledamemo.
Hereisa“memoized”versionoffibonacci:
known = {0:0, 1:1}
def fibonacci(n):
if n in known:
return known[n]
res = fibonacci(n-1) + fibonacci(n-2)
known[n] = res
return res
knownisadictionarythatkeepstrackoftheFibonaccinumberswealreadyknow. Itstarts
withtwoitems: 0mapsto0and1mapsto1.

| 110 |     |     | Chapter11. | Dictionaries |
| --- | --- | --- | ---------- | ------------ |
Wheneverfibonacciiscalled,itchecksknown.
Iftheresultisalreadythere,itcanreturn
immediately. Otherwise it has to compute the new value, add it to the dictionary, and
returnit.
Ifyourunthisversionoffibonacciandcompareitwiththeoriginal,youwillfindthatit
ismuchfaster.
| 11.7 Global | variables |     |     |     |
| ----------- | --------- | --- | --- | --- |
Inthepreviousexample,knowniscreatedoutsidethefunction,soitbelongstothespecial
| __main__. |     | __main__ |     |     |
| --------- | --- | -------- | --- | --- |
frame called Variables in are sometimes called global because they
can be accessed from any function. Unlike local variables, which disappear when their
functionends,globalvariablespersistfromonefunctioncalltothenext.
Itiscommontouseglobalvariablesforflags;thatis,booleanvariablesthatindicate(“flag”)
verbose
whether a condition is true. For example, some programs use a flag named to
controlthelevelofdetailintheoutput:
| verbose = True |     |     |     |     |
| -------------- | --- | --- | --- | --- |
def example1():
if verbose:
print('Running example1')
Ifyoutrytoreassignaglobalvariable,youmightbesurprised. Thefollowingexampleis
supposedtokeeptrackofwhetherthefunctionhasbeencalled:
| been_called = | False |     |     |     |
| ------------- | ----- | --- | --- | --- |
def example2():
| been_called | = True | # WRONG |     |     |
| ----------- | ------ | ------- | --- | --- |
Butifyourunityouwillseethatthevalueofbeen_calleddoesn’tchange.
Theproblem
isthatexample2createsanewlocalvariablenamedbeen_called.
Thelocalvariablegoes
awaywhenthefunctionends,andhasnoeffectontheglobalvariable.
Toreassignaglobalvariableinsideafunctionyouhavetodeclaretheglobalvariablebefore
youuseit:
| been_called = | False |     |     |     |
| ------------- | ----- | --- | --- | --- |
def example2():
| global been_called |        |     |     |     |
| ------------------ | ------ | --- | --- | --- |
| been_called        | = True |     |     |     |
The global statement tells the interpreter something like, “In this function, when I say
been_called,Imeantheglobalvariable;don’tcreatealocalone.”
Here’sanexamplethattriestoupdateaglobalvariable:
count = 0
def example3():
| count = count | + 1 | # WRONG |     |     |
| ------------- | --- | ------- | --- | --- |
Ifyourunityouget:

11.8. Debugging 111
UnboundLocalError: local variable 'count' referenced before assignment
Python assumes that count is local, and under that assumption you are reading it before
writingit. Thesolution,again,istodeclarecountglobal.
def example3():
global count
count += 1
Ifaglobalvariablereferstoamutablevalue,youcanmodifythevaluewithoutdeclaring
thevariable:
known = {0:0, 1:1}
def example4():
known[2] = 1
Soyoucanadd,removeandreplaceelementsofagloballistordictionary,butifyouwant
toreassignthevariable,youhavetodeclareit:
def example5():
global known
known = dict()
Global variables can be useful, but if you have a lot of them, and you modify them fre-
quently,theycanmakeprogramshardtodebug.
11.8 Debugging
Asyouworkwithbiggerdatasetsitcanbecomeunwieldytodebugbyprintingandcheck-
ingtheoutputbyhand. Herearesomesuggestionsfordebugginglargedatasets:
Scaledowntheinput: If possible, reduce the size of the dataset. For example if the pro-
gram reads a text file, start with just the first 10 lines, or with the smallest example
youcanfind. Youcaneithereditthefilesthemselves,or(better)modifytheprogram
soitreadsonlythefirstnlines.
Ifthereisanerror,youcanreducentothesmallestvaluethatmanifeststheerror,and
thenincreaseitgraduallyasyoufindandcorrecterrors.
Checksummariesandtypes: Insteadofprintingandcheckingtheentiredataset,consider
printingsummariesofthedata: forexample,thenumberofitemsinadictionaryor
thetotalofalistofnumbers.
Acommoncauseofruntimeerrorsisavaluethatisnottherighttype.Fordebugging
thiskindoferror,itisoftenenoughtoprintthetypeofavalue.
Writeself-checks: Sometimes you can write code to check for errors automatically. For
example,ifyouarecomputingtheaverageofalistofnumbers,youcouldcheckthat
the result is not greater than the largest element in the list or less than the smallest.
Thisiscalleda“sanitycheck”becauseitdetectsresultsthatare“insane”.
Another kind of check compares the results of two different computations to see if
theyareconsistent. Thisiscalleda“consistencycheck”.

112 Chapter11. Dictionaries
Formattheoutput: Formattingdebuggingoutputcanmakeiteasiertospotanerror. We
sawanexampleinSection6.9.Anothertoolyoumightfindusefulisthepprintmod-
ule,whichprovidesapprintfunctionthatdisplaysbuilt-intypesinamorehuman-
readableformat(pprintstandsfor“prettyprint”).
Again,timeyouspendbuildingscaffoldingcanreducethetimeyouspenddebugging.
11.9 Glossary
mapping: A relationship in which each element of one set corresponds to an element of
anotherset.
dictionary: Amappingfromkeystotheircorrespondingvalues.
key-valuepair: Therepresentationofthemappingfromakeytoavalue.
item: Inadictionary,anothernameforakey-valuepair.
key: Anobjectthatappearsinadictionaryasthefirstpartofakey-valuepair.
value: Anobjectthatappearsinadictionaryasthesecondpartofakey-valuepair. Thisis
morespecificthanourprevioususeoftheword“value”.
implementation: Awayofperformingacomputation.
hashtable: ThealgorithmusedtoimplementPythondictionaries.
hashfunction: Afunctionusedbyahashtabletocomputethelocationforakey.
hashable: Atypethathasahashfunction.Immutabletypeslikeintegers,floatsandstrings
arehashable;mutabletypeslikelistsanddictionariesarenot.
lookup: Adictionaryoperationthattakesakeyandfindsthecorrespondingvalue.
reverselookup: Adictionaryoperationthattakesavalueandfindsoneormorekeysthat
maptoit.
raisestatement: Astatementthat(deliberately)raisesanexception.
singleton: Alist(orothersequence)withasingleelement.
callgraph: Adiagramthatshowseveryframecreatedduringtheexecutionofaprogram,
withanarrowfromeachcallertoeachcallee.
memo: Acomputedvaluestoredtoavoidunnecessaryfuturecomputation.
globalvariable: A variable defined outside a function. Global variables can be accessed
fromanyfunction.
globalstatement: Astatementthatdeclaresavariablenameglobal.
flag: Abooleanvariableusedtoindicatewhetheraconditionistrue.
declaration: Astatementlikeglobalthattellstheinterpretersomethingaboutavariable.

11.10. Exercises 113
11.10 Exercises
Exercise11.1. Writeafunctionthatreadsthewordsinwords.txtandstoresthemaskeysina
dictionary. Itdoesn’tmatterwhatthevaluesare. Thenyoucanusetheinoperatorasafastwayto
checkwhetherastringisinthedictionary.
IfyoudidExercise10.10,youcancomparethespeedofthisimplementationwiththelistinoperator
andthebisectionsearch.
Exercise11.2. Readthedocumentationofthedictionarymethodsetdefaultanduseittowritea
moreconciseversionofinvert_dict. Solution: https://thinkpython.com/code/invert_
dict.py.
Exercise 11.3. Memoize the Ackermann function from Exercise 6.2 and see if memoization
makes it possible to evaluate the function with bigger arguments. Hint: no. Solution: https:
//thinkpython.com/code/ackermann_memo.py.
Exercise11.4. IfyoudidExercise10.7,youalreadyhaveafunctionnamedhas_duplicatesthat
takesalistasaparameterandreturnsTrueifthereisanyobjectthatappearsmorethanonceinthe
list.
Use a dictionary to write a faster, simpler version of has_duplicates. Solution: https://
thinkpython.com/code/has_duplicates.py.
Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and get the other (see
rotate_wordinExercise8.5).
Write a program that reads a wordlist and finds all the rotate pairs. Solution: https://
thinkpython.com/code/rotate_pairs.py.
Exercise11.6. Here’sanotherPuzzlerfromCarTalk(http://www.cartalk.com/content/
puzzlers):
ThiswassentinbyafellownamedDanO’Leary.Hecameuponacommonone-syllable,
five-letterwordrecentlythathasthefollowinguniqueproperty. Whenyouremovethe
firstletter,theremaininglettersformahomophoneoftheoriginalword,thatisaword
that sounds exactly the same. Replace the first letter, that is, put it back and remove
thesecondletterandtheresultisyetanotherhomophoneoftheoriginalword. Andthe
questionis,what’stheword?
Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter
word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first
letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the
rackonthatbuck! Itmusthavebeenanine-pointer!’ It’saperfecthomophone. Ifyou
putthe‘w’back,andremovethe‘r,’instead,you’releftwiththeword,‘wack,’whichis
arealword,it’sjustnotahomophoneoftheothertwowords.
Butthereis,however,atleastonewordthatDanandweknowof,whichwillyieldtwo
homophones if you remove either of the first two letters to make two, new four-letter
words. Thequestionis,what’stheword?
YoucanusethedictionaryfromExercise11.1tocheckwhetherastringisinthewordlist.
To check whether two words are homophones, you can use the CMU Pronouncing
Dictionary. You can download it from http://www.speech.cs.cmu.edu/cgi-bin/
cmudict or from https://thinkpython.com/code/c06d and you can also down-
load https://thinkpython.com/code/pronounce.py, which provides a function named
read_dictionary that reads the pronouncing dictionary and returns a Python dictionary that
mapsfromeachwordtoastringthatdescribesitsprimarypronunciation.

| 114 | Chapter11. | Dictionaries |
| --- | ---------- | ------------ |
WriteaprogramthatlistsallthewordsthatsolvethePuzzler.Solution:https://thinkpython.
com/code/homophone.py.

| Chapter | 12  |     |
| ------- | --- | --- |
Tuples
Thischapterpresentsonemorebuilt-intype,thetuple,andthenshowshowlists,dictionar-
ies,andtuplesworktogether. Ialsopresentausefulfeatureforvariable-lengthargument
lists,thegatherandscatteroperators.
One note: there is no consensus on how to pronounce “tuple”. Some people say “tuh-
ple”, which rhymes with “supple”. But in the context of programming, most people say
“too-ple”,whichrhymeswith“quadruple”.
| 12.1 Tuples | are | immutable |
| ----------- | --- | --------- |
A tuple is a sequence of values. The values can be any type, and they are indexed by
integers,sointhatrespecttuplesarealotlikelists. Theimportantdifferenceisthattuples
areimmutable.
Syntactically,atupleisacomma-separatedlistofvalues:
| >>> t = 'a', | 'b', 'c', | 'd', 'e' |
| ------------ | --------- | -------- |
Althoughitisnotnecessary,itiscommontoenclosetuplesinparentheses:
| >>> t = ('a', | 'b', 'c', | 'd', 'e') |
| ------------- | --------- | --------- |
Tocreateatuplewithasingleelement,youhavetoincludeafinalcomma:
| >>> t1 = 'a', |     |     |
| ------------- | --- | --- |
>>> type(t1)
<class 'tuple'>
Avalueinparenthesesisnotatuple:
| >>> t2 = ('a') |     |     |
| -------------- | --- | --- |
>>> type(t2)
<class 'str'>
Anotherwaytocreateatupleisthebuilt-infunctiontuple.
Withnoargument,itcreates
anemptytuple:
| >>> t = tuple() |     |     |
| --------------- | --- | --- |
>>> t
()

| 116 |     |     |     | Chapter12. | Tuples |
| --- | --- | --- | --- | ---------- | ------ |
Iftheargumentisasequence(string,listortuple),theresultisatuplewiththeelementsof
thesequence:
| >>> t = | tuple('lupins') |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- |
>>> t
| ('l', 'u', | 'p', 'i', | 'n', 's') |     |     |     |
| ---------- | --------- | --------- | --- | --- | --- |
tuple
Because is the name of a built-in function, you should avoid using it as a variable
name.
Mostlistoperatorsalsoworkontuples. Thebracketoperatorindexesanelement:
| >>> t = | ('a', 'b', | 'c', 'd', 'e') |     |     |     |
| ------- | ---------- | -------------- | --- | --- | --- |
>>> t[0]
'a'
Andthesliceoperatorselectsarangeofelements.
>>> t[1:3]
('b', 'c')
Butifyoutrytomodifyoneoftheelementsofthetuple,yougetanerror:
| >>> t[0]   | = 'A'  |                      |            |     |     |
| ---------- | ------ | -------------------- | ---------- | --- | --- |
| TypeError: | object | doesn't support item | assignment |     |     |
Because tuples are immutable, you can’t modify the elements. But you can replace one
tuplewithanother:
| >>> t = | ('A',) + t[1:] |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
>>> t
| ('A', 'b', | 'c', 'd', | 'e') |     |     |     |
| ---------- | --------- | ---- | --- | --- | --- |
Thisstatementmakesanewtupleandthenmakestrefertoit.
Therelationaloperatorsworkwithtuplesandothersequences;Pythonstartsbycomparing
thefirstelementfromeachsequence. Iftheyareequal,itgoesontothenextelements,and
so on, until itfinds elements thatdiffer. Subsequent elementsare notconsidered (even if
theyarereallybig).
| >>> (0, | 1, 2) < (0, | 3, 4) |     |     |     |
| ------- | ----------- | ----- | --- | --- | --- |
True
| >>> (0, | 1, 2000000) | < (0, 3, 4) |     |     |     |
| ------- | ----------- | ----------- | --- | --- | --- |
True
| 12.2 | Tuple assignment |     |     |     |     |
| ---- | ---------------- | --- | --- | --- | --- |
Itisoftenusefultoswapthevaluesoftwovariables. Withconventionalassignments,you
Forexample,toswapaandb:
havetouseatemporaryvariable.
| >>> temp | = a  |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- |
| >>> a =  | b    |     |     |     |     |
| >>> b =  | temp |     |     |     |     |
Thissolutioniscumbersome;tupleassignmentismoreelegant:
| >>> a, b | = b, a |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |

12.3. Tuplesasreturnvalues 117
The left side is a tuple of variables; the right side is a tuple of expressions. Each value
is assigned to its respective variable. All the expressions on the right side are evaluated
beforeanyoftheassignments.
Thenumberofvariablesontheleftandthenumberofvaluesontherighthavetobethe
same:
| >>> a,      | b = 1, 2, 3     |           |
| ----------- | --------------- | --------- |
| ValueError: | too many values | to unpack |
Moregenerally,therightsidecanbeanykindofsequence(string,listortuple). Forexam-
ple,tosplitanemailaddressintoausernameandadomain,youcouldwrite:
| >>> addr   | = 'monty@python.org'     |     |
| ---------- | ------------------------ | --- |
| >>> uname, | domain = addr.split('@') |     |
The return value from split is a list with two elements; the first element is assigned to
uname,thesecondtodomain.
>>> uname
'monty'
>>> domain
'python.org'
| 12.3 | Tuples as return | values |
| ---- | ---------------- | ------ |
Strictlyspeaking,afunctioncanonlyreturnonevalue,butifthevalueisatuple,theeffect
isthesameasreturningmultiplevalues. Forexample,ifyouwanttodividetwointegers
andcomputethequotientandremainder,itisinefficienttocomputex//yandthenx%y. It
isbettertocomputethembothatthesametime.
The built-in function divmod takes two arguments and returns a tuple of two values, the
| quotientandremainder. | Youcanstoretheresultasatuple: |     |
| --------------------- | ----------------------------- | --- |
| >>> t =               | divmod(7, 3)                  |     |
>>> t
(2, 1)
Orusetupleassignmenttostoretheelementsseparately:
| >>> quot, | rem = divmod(7, | 3)  |
| --------- | --------------- | --- |
>>> quot
2
>>> rem
1
Hereisanexampleofafunctionthatreturnsatuple:
def min_max(t):
| return | min(t), max(t) |     |
| ------ | -------------- | --- |
maxandminarebuilt-infunctionsthatfindthelargestandsmallestelementsofasequence.
min_maxcomputesbothandreturnsatupleoftwovalues.

| 118  |                 |          |        |     | Chapter12. | Tuples |
| ---- | --------------- | -------- | ------ | --- | ---------- | ------ |
| 12.4 | Variable-length | argument | tuples |     |            |        |
Functions can take a variable number of arguments. A parameter name that begins with
*gathersargumentsintoatuple. Forexample,printalltakesanynumberofarguments
andprintsthem:
def printall(*args):
print(args)
Thegatherparametercanhaveanynameyoulike, butargsisconventional. Here’show
thefunctionworks:
| >>> printall(1, | 2.0, | '3') |     |     |     |     |
| --------------- | ---- | ---- | --- | --- | --- | --- |
| (1, 2.0,        | '3') |      |     |     |     |     |
Thecomplementofgatherisscatter.Ifyouhaveasequenceofvaluesandyouwanttopass
|     |     |     |     | *   |     | divmod |
| --- | --- | --- | --- | --- | --- | ------ |
it to a function as multiple arguments, you can use the operator. For example,
takesexactlytwoarguments;itdoesn’tworkwithatuple:
| >>> t = | (7, 3) |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --- |
>>> divmod(t)
| TypeError: | divmod expected | 2 arguments, | got | 1   |     |     |
| ---------- | --------------- | ------------ | --- | --- | --- | --- |
Butifyouscatterthetuple,itworks:
>>> divmod(*t)
(2, 1)
Forexample,maxand
Manyofthebuilt-infunctionsusevariable-lengthargumenttuples.
mincantakeanynumberofarguments:
| >>> max(1, | 2, 3) |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- |
3
Butsumdoesnot.
| >>> sum(1, | 2, 3)        |         |              |       |     |     |
| ---------- | ------------ | ------- | ------------ | ----- | --- | --- |
| TypeError: | sum expected | at most | 2 arguments, | got 3 |     |     |
As an exercise, write a function called sum_all that takes any number of arguments and
returnstheirsum.
| 12.5 | Lists and tuples |     |     |     |     |     |
| ---- | ---------------- | --- | --- | --- | --- | --- |
zipisabuilt-infunctionthattakestwoormoresequencesandinterleavesthem.Thename
ofthefunctionreferstoazipper,whichinterleavestworowsofteeth.
Thisexamplezipsastringandalist:
| >>> s =     | 'abc'              |     |     |     |     |     |
| ----------- | ------------------ | --- | --- | --- | --- | --- |
| >>> t =     | [0, 1, 2]          |     |     |     |     |     |
| >>> zip(s,  | t)                 |     |     |     |     |     |
| <zip object | at 0x7f7d0a9e7c48> |     |     |     |     |     |
Theresultisazipobjectthatknowshowtoiteratethroughthepairs. Themostcommon
useofzipisinaforloop:

12.5. Listsandtuples 119
| >>> for | pair in zip(s, | t): |     |
| ------- | -------------- | --- | --- |
| ...     | print(pair)    |     |     |
...
('a', 0)
('b', 1)
('c', 2)
A zip object is a kind of iterator, which is any object that iterates through a sequence.
Iteratorsaresimilartolistsinsomeways,butunlikelists,youcan’tuseanindextoselect
anelementfromaniterator.
Ifyouwanttouselistoperatorsandmethods,youcanuseazipobjecttomakealist:
| >>> list(zip(s, | t))       |           |     |
| --------------- | --------- | --------- | --- |
| [('a', 0),      | ('b', 1), | ('c', 2)] |     |
Theresultisalistoftuples;inthisexample,eachtuplecontainsacharacterfromthestring
andthecorrespondingelementfromthelist.
Ifthesequencesarenotthesamelength,theresulthasthelengthoftheshorterone.
| >>> list(zip('Anne', |       | 'Elk'))     |       |
| -------------------- | ----- | ----------- | ----- |
| [('A', 'E'),         | ('n', | 'l'), ('n', | 'k')] |
Youcanusetupleassignmentinaforlooptotraversealistoftuples:
| t = [('a',    | 0), ('b', | 1), ('c', | 2)] |
| ------------- | --------- | --------- | --- |
| for letter,   | number    | in t:     |     |
| print(number, |           | letter)   |     |
Each time through the loop, Python selects the next tuple in the list and assigns the ele-
| mentstoletterandnumber. |     | Theoutputofthisloopis: |     |
| ----------------------- | --- | ---------------------- | --- |
0 a
1 b
2 c
Ifyoucombinezip, forandtupleassignment, yougetausefulidiomfortraversingtwo
has_match t1
(or more) sequences at the same time. For example, takes two sequences,
andt2,andreturnsTrueifthereisanindexisuchthatt1[i] == t2[i]:
| def has_match(t1, |                 | t2): |     |
| ----------------- | --------------- | ---- | --- |
| for               | x, y in zip(t1, | t2): |     |
if x == y:
|        | return | True |     |
| ------ | ------ | ---- | --- |
| return | False  |      |     |
Ifyouneedtotraversetheelementsofasequenceandtheirindices,youcanusethebuilt-in
functionenumerate:
| for index,   | element  | in enumerate('abc'): |     |
| ------------ | -------- | -------------------- | --- |
| print(index, | element) |                      |     |
Theresultfromenumerateisanenumerateobject,whichiteratesasequenceofpairs;each
pair contains an index (starting from 0) and an element from the given sequence. In this
example,theoutputis
0 a
1 b
2 c
Again.

| 120               |     |            |     | Chapter12. | Tuples |
| ----------------- | --- | ---------- | --- | ---------- | ------ |
| 12.6 Dictionaries |     | and tuples |     |            |        |
Dictionaries have a method called items that returns a sequence of tuples, where each
tupleisakey-valuepair.
| >>> d = {'a':0,   | 'b':1, | 'c':2} |     |     |     |
| ----------------- | ------ | ------ | --- | --- | --- |
| >>> t = d.items() |        |        |     |     |     |
>>> t
| dict_items([('c', | 2), | ('a', 0), | ('b', 1)]) |     |     |
| ----------------- | --- | --------- | ---------- | --- | --- |
Theresultisadict_itemsobject,whichisaniteratorthatiteratesthekey-valuepairs.
You
canuseitinaforlooplikethis:
| >>> for key,   | value in | d.items(): |     |     |     |
| -------------- | -------- | ---------- | --- | --- | --- |
| ... print(key, | value)   |            |     |     |     |
...
c 2
a 0
b 1
Asyoushouldexpectfromadictionary,theitemsareinnoparticularorder.
Goingintheotherdirection,youcanusealistoftuplestoinitializeanewdictionary:
| >>> t = [('a',  | 0), ('c', | 2), ('b', | 1)] |     |     |
| --------------- | --------- | --------- | --- | --- | --- |
| >>> d = dict(t) |           |           |     |     |     |
>>> d
| {'a': 0, 'c': | 2, 'b': | 1}  |     |     |     |
| ------------- | ------- | --- | --- | --- | --- |
Combiningdictwithzipyieldsaconcisewaytocreateadictionary:
| >>> d = dict(zip('abc', |     | range(3))) |     |     |     |
| ----------------------- | --- | ---------- | --- | --- | --- |
>>> d
| {'a': 0, 'c': | 2, 'b': | 1}  |     |     |     |
| ------------- | ------- | --- | --- | --- | --- |
Thedictionarymethodupdatealsotakesalistoftuplesandaddsthem,askey-valuepairs,
toanexistingdictionary.
Itiscommontousetuplesaskeysindictionaries(primarilybecauseyoucan’tuselists).For
example, a telephone directory might map from last-name, first-name pairs to telephone
Assumingthatwehavedefinedlast,firstandnumber,wecouldwrite:
numbers.
| directory[last, | first] | = number |     |     |     |
| --------------- | ------ | -------- | --- | --- | --- |
Theexpressioninbracketsisatuple. Wecouldusetupleassignmenttotraversethisdic-
tionary.
| for last, first | in directory: |                        |     |     |     |
| --------------- | ------------- | ---------------------- | --- | --- | --- |
| print(first,    | last,         | directory[last,first]) |     |     |     |
Thislooptraversesthekeysindirectory,whicharetuples.
Itassignstheelementsofeach
tupletolastandfirst,thenprintsthenameandcorrespondingtelephonenumber.
There are two ways to represent tuples in a state diagram. The more detailed version
shows the indices and elements just as they appear in a list. For example, the tuple
| ('Cleese', 'John')wouldappearasinFigure12.1. |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- |
Butinalargerdiagramyoumightwanttoleaveoutthedetails. Forexample,adiagramof
thetelephonedirectorymightappearasinFigure12.2.
Here the tuples are shown using Python syntax as a graphical shorthand. The telephone
numberinthediagramisthecomplaintslinefortheBBC,sopleasedon’tcallit.

12.7. Sequencesofsequences 121
tuple
0 ’Cleese’
1 ’John’
Figure12.1: Statediagram.
dict
(’Cleese’, ’John’) ’08700 100 222’
(’Chapman’, ’Graham’) ’08700 100 222’
(’Idle’, ’Eric’) ’08700 100 222’
(’Gilliam’, ’Terry’) ’08700 100 222’
(’Jones’, ’Terry’) ’08700 100 222’
(’Palin’, ’Michael’) ’08700 100 222’
Figure12.2: Statediagram.
12.7 Sequences of sequences
I have focused on lists of tuples, but almost all of the examples in this chapter also work
with lists of lists, tuples of tuples, and tuples of lists. To avoid enumerating the possible
combinations,itissometimeseasiertotalkaboutsequencesofsequences.
In many contexts, the different kinds of sequences (strings, lists and tuples) can be used
interchangeably. Sohowshouldyouchooseoneovertheothers?
To start with the obvious, strings are more limited than other sequences because the ele-
mentshavetobecharacters. Theyarealsoimmutable. Ifyouneedtheabilitytochangethe
charactersinastring(asopposedtocreatinganewstring),youmightwanttousealistof
charactersinstead.
Listsaremorecommonthantuples,mostlybecausetheyaremutable. Butthereareafew
caseswhereyoumightprefertuples:
1. Insomecontexts,likeareturnstatement,itissyntacticallysimplertocreateatuple
thanalist.
2. Ifyouwanttouseasequenceasadictionarykey,youhavetouseanimmutabletype
likeatupleorstring.
3. Ifyouarepassingasequenceasanargumenttoafunction,usingtuplesreducesthe
potentialforunexpectedbehaviorduetoaliasing.
Becausetuplesareimmutable,theydon’tprovidemethodslikesortandreverse,which
modify existing lists. But Python provides the built-in function sorted, which takes any
sequence and returns a new list with the same elements in sorted order, and reversed,
whichtakesasequenceandreturnsaniteratorthattraversesthelistinreverseorder.

| 122 |     |     |     |     | Chapter12. | Tuples |
| --- | --- | --- | --- | --- | ---------- | ------ |
12.8 Debugging
Lists,dictionariesandtuplesareexamplesofdatastructures;inthischapterwearestarting
toseecompounddatastructures, likelistsoftuples,ordictionariesthatcontaintuplesas
keysandlistsasvalues. Compounddatastructuresareuseful,buttheyarepronetowhat
Icallshapeerrors;thatis,errorscausedwhenadatastructurehasthewrongtype,size,or
structure. Forexample,ifyouareexpectingalistwithoneintegerandIgiveyouaplain
oldinteger(notinalist),itwon’twork.
structshape
To help debug these kinds of errors, I have written a module called that
provides a function, also called structshape, that takes any kind of data structure as
an argument and returns a string that summarizes its shape. You can download it from
https://thinkpython.com/code/structshape.py
Here’stheresultforasimplelist:
| >>> from | structshape | import structshape |     |     |     |     |
| -------- | ----------- | ------------------ | --- | --- | --- | --- |
| >>> t =  | [1, 2, 3]   |                    |     |     |     |     |
>>> structshape(t)
| 'list of | 3 int' |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- |
A fancier program might write “list of 3 ints”, but it was easier not to deal with plurals.
Here’salistoflists:
| >>> t2 = | [[1,2], [3,4], | [5,6]] |     |     |     |     |
| -------- | -------------- | ------ | --- | --- | --- | --- |
>>> structshape(t2)
| 'list of | 3 list of | 2 int' |     |     |     |     |
| -------- | --------- | ------ | --- | --- | --- | --- |
structshape
If the elements of the list are not the same type, groups them, in order, by
type:
| >>> t3 = | [1, 2, 3, | 4.0, '5', '6', | [7], [8], | 9]  |     |     |
| -------- | --------- | -------------- | --------- | --- | --- | --- |
>>> structshape(t3)
| 'list of | (3 int, float, | 2 str, | 2 list of | int, int)' |     |     |
| -------- | -------------- | ------ | --------- | ---------- | --- | --- |
Here’salistoftuples:
| >>> s =  | 'abc'       |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
| >>> lt = | list(zip(t, | s)) |     |     |     |     |
>>> structshape(lt)
| 'list of | 3 tuple of | (int, str)' |     |     |     |     |
| -------- | ---------- | ----------- | --- | --- | --- | --- |
Andhere’sadictionarywith3itemsthatmapintegerstostrings.
| >>> d = | dict(lt) |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- |
>>> structshape(d)
| 'dict of | 3 int->str' |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
Ifyouarehavingtroublekeepingtrackofyourdatastructures,structshapecanhelp.
12.9 Glossary
tuple: Animmutablesequenceofelements.
tupleassignment: An assignment with a sequence on the right side and a tuple of vari-
ablesontheleft. Therightsideisevaluatedandthenitselementsareassignedtothe
variablesontheleft.

12.10. Exercises 123
gather: Anoperationthatcollectsmultipleargumentsintoatuple.
scatter: Anoperationthatmakesasequencebehavelikemultiplearguments.
zipobject: The result of calling a built-in function zip; an object that iterates through a
sequenceoftuples.
iterator: An object that can iterate through a sequence, but which does not provide list
operatorsandmethods.
datastructure: Acollectionofrelatedvalues,oftenorganizedinlists,dictionaries,tuples,
etc.
shapeerror: Anerrorcausedbecauseavaluehasthewrongshape;thatis,thewrongtype
orsize.
12.10 Exercises
Exercise 12.1. Write a function called most_frequent that takes a string and prints the let-
ters in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http:
//en.wikipedia.org/wiki/Letter_frequencies. Solution: https://thinkpython.
com/code/most_frequent.py.
Exercise12.2. Moreanagrams!
1. Writeaprogramthatreadsawordlistfromafile(seeSection9.1)andprintsallthesetsof
wordsthatareanagrams.
Hereisanexampleofwhattheoutputmightlooklike:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of letters to a list
of words that can be spelled with those letters. The question is, how can you represent the
collectionoflettersinawaythatcanbeusedasakey?
2. Modifythepreviousprogramsothatitprintsthelongestlistofanagramsfirst, followedby
thesecondlongest,andsoon.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What collection of 8 letters forms the most possible
bingos?
Solution: https://thinkpython.com/code/anagram_sets.py.
Exercise 12.3. Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
themetathesispairsinthedictionary. Hint: don’ttestallpairsofwords,anddon’ttestallpossible
swaps. Solution: https://thinkpython.com/code/metathesis.py. Credit: This exercise
isinspiredbyanexampleathttp://puzzlers.org.

124 Chapter12. Tuples
Exercise 12.4. Here’s another Car Talk Puzzler (http://www.cartalk.com/content/
puzzlers):
WhatisthelongestEnglishword,thatremainsavalidEnglishword,asyouremoveits
lettersoneatatime?
Now,letterscanberemovedfromeitherend,orthemiddle,butyoucan’trearrangeany
oftheletters. Everytimeyoudropaletter,youwindupwithanotherEnglishword. If
you do that, you’re eventually going to wind up with one letter and that too is going
tobeanEnglishword—onethat’sfoundinthedictionary. Iwanttoknowwhat’sthe
longestwordandhowmanylettersdoesithave?
I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
you take a letter off, one from the interior of the word, take the r away, and we’re left
withthewordspite,thenwetaketheeofftheend,we’releftwithspit,wetakethesoff,
we’releftwithpit,it,andI.
Writeaprogramtofindallwordsthatcanbereducedinthisway,andthenfindthelongestone.
Thisexerciseisalittlemorechallengingthanmost,soherearesomesuggestions:
1. Youmightwanttowriteafunctionthattakesawordandcomputesalistofallthewordsthat
canbeformedbyremovingoneletter. Thesearethe“children”oftheword.
2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can
considertheemptystringreducible.
3. ThewordlistIprovided,words.txt,doesn’tcontainsingleletterwords. Soyoumightwant
toadd“I”,“a”,andtheemptystring.
4. Toimprovetheperformanceofyourprogram,youmightwanttomemoizethewordsthatare
knowntobereducible.
Solution: https://thinkpython.com/code/reducible.py.

Chapter 13
Case study: data structure
selection
At this point you have learned about Python’s core data structures, and you have seen
someofthealgorithmsthatusethem. Ifyouwouldliketoknowmoreaboutalgorithms,
thismightbeagoodtimetoreadChapterB.Butyoudon’thavetoreaditbeforeyougo
on;youcanreaditwheneveryouareinterested.
This chapter presents a case study with exercises that let you think about choosing data
structuresandpracticeusingthem.
13.1 Word frequency analysis
Asusual,youshouldatleastattempttheexercisesbeforeyoureadmysolutions.
Exercise13.1. Writeaprogramthatreadsafile,breakseachlineintowords,stripswhitespaceand
punctuationfromthewords,andconvertsthemtolowercase.
Hint: Thestringmoduleprovidesastringnamedwhitespace,whichcontainsspace,tab,new-
line, etc., and punctuation which contains the punctuation characters. Let’s see if we can make
Pythonswear:
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
Also,youmightconsiderusingthestringmethodsstrip,replaceandtranslate.
Exercise13.2. GotoProjectGutenberg(http://gutenberg.org)anddownloadyourfavorite
out-of-copyrightbookinplaintextformat.
Modify your program from the previous exercise to read the book you downloaded, skip over the
headerinformationatthebeginningofthefile,andprocesstherestofthewordsasbefore.
Thenmodifytheprogramtocountthetotalnumberofwordsinthebook,andthenumberoftimes
eachwordisused.
Printthenumberofdifferentwordsusedinthebook. Comparedifferentbooksbydifferentauthors,
writtenindifferenteras. Whichauthorusesthemostextensivevocabulary?

126 Chapter13. Casestudy: datastructureselection
Exercise13.3. Modifytheprogramfromthepreviousexercisetoprintthe20mostfrequentlyused
wordsinthebook.
Exercise13.4. Modifythepreviousprogramtoreadawordlist(seeSection9.1)andthenprintall
the words in the book that are not in the word list. How many of them are typos? How many of
themarecommonwordsthatshouldbeinthewordlist,andhowmanyofthemarereallyobscure?
13.2 Random numbers
Given the same inputs, most computer programs generate the same outputs every time,
sotheyaresaidtobedeterministic. Determinismisusuallyagoodthing,sinceweexpect
thesamecalculationtoyieldthesameresult. Forsomeapplications,though,wewantthe
computertobeunpredictable. Gamesareanobviousexample,buttherearemore.
Making a program truly nondeterministic turns out to be difficult, but there are ways to
make it at least seem nondeterministic. One of them is to use algorithms that generate
pseudorandomnumbers. Pseudorandomnumbersarenottrulyrandombecausetheyare
generatedbyadeterministiccomputation, butjustbylookingatthenumbersitisallbut
impossibletodistinguishthemfromrandom.
The random module provides functions that generate pseudorandom numbers (which I
willsimplycall“random”fromhereon).
Thefunctionrandomreturnsarandomfloatbetween0.0and1.0(including0.0butnot1.0).
Eachtimeyoucallrandom,yougetthenextnumberinalongseries. Toseeasample,run
thisloop:
import random
for i in range(10):
x = random.random()
print(x)
Thefunctionrandinttakesparameterslowandhighandreturnsanintegerbetweenlow
andhigh(includingboth).
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
9
Tochooseanelementfromasequenceatrandom,youcanusechoice:
>>> t = [1, 2, 3]
>>> random.choice(t)
2
>>> random.choice(t)
3
The random module also provides functions to generate random values from continuous
distributionsincludingGaussian,exponential,gamma,andafewmore.
Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in
Section11.2andreturnsarandomvaluefromthehistogram,chosenwithprobabilityinproportion
tofrequency. Forexample,forthishistogram:

| 13.3. Wordhistogram |      |     |     |     | 127 |
| ------------------- | ---- | --- | --- | --- | --- |
| >>> t = ['a', 'a',  | 'b'] |     |     |     |     |
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}
yourfunctionshouldreturn'a'withprobability2/3and'b'withprobability1/3.
13.3 Word histogram
You should attempt the previous exercises before you go on. You can download my
solution from https://thinkpython.com/code/analyze_book1.py. You will also need
https://thinkpython.com/code/emma.txt.
Hereisaprogramthatreadsafileandbuildsahistogramofthewordsinthefile:
import string
def process_file(filename):
hist = dict()
fp = open(filename)
| for line in | fp: |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
process_line(line, hist)
return hist
| def process_line(line,               | hist):        |                      |     |     |     |
| ------------------------------------ | ------------- | -------------------- | --- | --- | --- |
| line = line.replace('-',             | ' ')          |                      |     |     |     |
| for word in                          | line.split(): |                      |     |     |     |
| word = word.strip(string.punctuation |               | + string.whitespace) |     |     |     |
word = word.lower()
| hist[word] | = hist.get(word, | 0) + 1 |     |     |     |
| ---------- | ---------------- | ------ | --- | --- | --- |
hist = process_file('emma.txt')
Thisprogramreadsemma.txt,whichcontainsthetextofEmmabyJaneAusten.
process_file
| loops | through the lines | of the file, passing | them one | at a time | to  |
| ----- | ----------------- | -------------------- | -------- | --------- | --- |
process_line. Thehistogramhistisbeingusedasanaccumulator.
process_lineusesthestringmethodreplacetoreplacehyphenswithspacesbeforeusing
split strip
to break the line into a list of strings. It traverses the list of words and uses
andlowertoremovepunctuationandconverttolowercase. (Itisashorthandtosaythat
stringsare“converted”;rememberthatstringsareimmutable,somethodslikestripand
lowerreturnnewstrings.)
Finally, process_line updates the histogram by creating a new item or incrementing an
existingone.
To count the total number of words in the file, we can add up the frequencies in the his-
togram:
def total_words(hist):
return sum(hist.values())

| 128 |     |     | Chapter13. | Casestudy: | datastructureselection |
| --- | --- | --- | ---------- | ---------- | ---------------------- |
Thenumberofdifferentwordsisjustthenumberofitemsinthedictionary:
def different_words(hist):
| return | len(hist) |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- |
Hereissomecodetoprinttheresults:
| print('Total  | number | of words:',        | total_words(hist))     |     |     |
| ------------- | ------ | ------------------ | ---------------------- | --- | --- |
| print('Number | of     | different words:', | different_words(hist)) |     |     |
Andtheresults:
| Total number | of words:    | 161080      |     |     |     |
| ------------ | ------------ | ----------- | --- | --- | --- |
| Number       | of different | words: 7214 |     |     |     |
| 13.4         | Most common  | words       |     |     |     |
Tofindthemostcommonwords,wecanmakealistoftuples,whereeachtuplecontainsa
wordanditsfrequency,andsortit.
Thefollowingfunctiontakesahistogramandreturnsalistofword-frequencytuples:
def most_common(hist):
| t = | []               |                  |     |     |     |
| --- | ---------------- | ---------------- | --- | --- | --- |
| for | key, value       | in hist.items(): |     |     |     |
|     | t.append((value, | key))            |     |     |     |
t.sort(reverse=True)
| return | t   |     |     |     |     |
| ------ | --- | --- | --- | --- | --- |
Ineachtuple,thefrequencyappearsfirst,sotheresultinglistissortedbyfrequency. Here
isaloopthatprintsthetenmostcommonwords:
t = most_common(hist)
| print('The  | most common | words are:') |     |     |     |
| ----------- | ----------- | ------------ | --- | --- | --- |
| for freq,   | word in     | t[:10]:      |     |     |     |
| print(word, | freq,       | sep='\t')    |     |     |     |
Iusethekeywordargumentseptotellprinttouseatabcharacterasa“separator”,rather
thanaspace,sothesecondcolumnislinedup. HerearetheresultsfromEmma:
| The most | common words | are: |     |     |     |
| -------- | ------------ | ---- | --- | --- | --- |
| to       | 5242         |      |     |     |     |
| the      | 5205         |      |     |     |     |
| and      | 4897         |      |     |     |     |
| of       | 4295         |      |     |     |     |
| i        | 3191         |      |     |     |     |
| a        | 3130         |      |     |     |     |
| it       | 2529         |      |     |     |     |
| her      | 2483         |      |     |     |     |
| was      | 2400         |      |     |     |     |
| she      | 2364         |      |     |     |     |
Thiscodecanbesimplifiedusingthekeyparameterofthesortfunction.
Ifyouarecuri-
ous,youcanreadaboutitathttps://wiki.python.org/moin/HowTo/Sorting.

13.5. Optionalparameters 129
| 13.5 Optional | parameters |     |     |     |
| ------------- | ---------- | --- | --- | --- |
Wehave seenbuilt-in functionsand methodsthat takeoptionalarguments. Itis possible
towriteprogrammer-definedfunctionswithoptionalarguments,too. Forexample,hereis
afunctionthatprintsthemostcommonwordsinahistogram
| def print_most_common(hist, |             | num=10):     |     |     |
| --------------------------- | ----------- | ------------ | --- | --- |
| t = most_common(hist)       |             |              |     |     |
| print('The                  | most common | words are:') |     |     |
| for freq,                   | word in     | t[:num]:     |     |     |
| print(word,                 | freq,       | sep='\t')    |     |     |
Thedefaultvalueofnumis10.
Thefirstparameterisrequired;thesecondisoptional.
Ifyouonlyprovideoneargument:
print_most_common(hist)
numgetsthedefaultvalue.
Ifyouprovidetwoarguments:
| print_most_common(hist, |     | 20) |     |     |
| ----------------------- | --- | --- | --- | --- |
num gets the value of the argument instead. In other words, the optional argument over-
ridesthedefaultvalue.
Ifafunctionhasbothrequiredandoptionalparameters,alltherequiredparametershave
tocomefirst,followedbytheoptionalones.
| 13.6 Dictionary |     | subtraction |     |     |
| --------------- | --- | ----------- | --- | --- |
Findingthewordsfromthebookthatarenotinthewordlistfromwords.txtisaproblem
youmightrecognizeassetsubtraction;thatis,wewanttofindallthewordsfromoneset
(thewordsinthebook)thatarenotintheother(thewordsinthelist).
subtract takes dictionaries d1 and d2 and returns a new dictionary that contains all the
keysfromd1thatarenotind2.
Sincewedon’treallycareaboutthevalues,wesetthemall
toNone.
| def subtract(d1, | d2):       |      |     |     |
| ---------------- | ---------- | ---- | --- | --- |
| res =            | dict()     |      |     |     |
| for key          | in d1:     |      |     |     |
| if               | key not in | d2:  |     |     |
|                  | res[key] = | None |     |     |
| return           | res        |      |     |     |
Tofindthewordsinthebookthatarenotinwords.txt,wecanuseprocess_filetobuild
ahistogramforwords.txt,andthensubtract:
| words = process_file('words.txt') |             |             |             |         |
| --------------------------------- | ----------- | ----------- | ----------- | ------- |
| diff = subtract(hist,             |             | words)      |             |         |
| print("Words                      | in the book | that aren't | in the word | list:") |
| for word in                       | diff:       |             |             |         |
| print(word,                       | end='       | ')          |             |         |
HerearesomeoftheresultsfromEmma:

| 130       |                  |            | Chapter13.       | Casestudy: | datastructureselection |
| --------- | ---------------- | ---------- | ---------------- | ---------- | ---------------------- |
| Words in  | the book that    | aren't     | in the word      | list:      |                        |
| rencontre | jane's blanche   | woodhouses | disingenuousness |            |                        |
| friend's  | venice apartment | ...        |                  |            |                        |
Someofthesewordsarenamesandpossessives. Others,like“rencontre”,arenolongerin
| commonuse. | Butafewarecommonwordsthatshouldreallybeinthelist! |     |     |     |     |
| ---------- | ------------------------------------------------- | --- | --- | --- | --- |
set
Exercise 13.6. Python provides a data structure called that provides many common set
operations. You can read about them in Section 19.5, or read the documentation at http:
//docs.python.org/3/library/stdtypes.html#types-set.
Write a program that uses set subtraction to find words in the book that are not in the word list.
Solution: https://thinkpython.com/code/analyze_book2.py.
| 13.7 | Random words |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- |
Tochoosearandomwordfromthehistogram,thesimplestalgorithmistobuildalistwith
multiplecopiesofeachword,accordingtotheobservedfrequency,andthenchoosefrom
thelist:
def random_word(h):
| t =    | []               |            |     |     |     |
| ------ | ---------------- | ---------- | --- | --- | --- |
| for    | word, freq in    | h.items(): |     |     |     |
|        | t.extend([word]  | * freq)    |     |     |     |
| return | random.choice(t) |            |     |     |     |
The expression [word] * freq creates a list with freq copies of the string word. The
extendmethodissimilartoappendexceptthattheargumentisasequence.
Thisalgorithmworks,butitisnotveryefficient;eachtimeyouchoosearandomword,it
rebuildsthelist,whichisasbigastheoriginalbook. Anobviousimprovementistobuild
thelistonceandthenmakemultipleselections,butthelistisstillbig.
Analternativeis:
1. Usekeystogetalistofthewordsinthebook.
2. Build a list that contains the cumulative sum of the word frequencies (see Exer-
cise10.2). Thelastiteminthislististhetotalnumberofwordsinthebook,n.
3. Choosearandomnumberfrom1ton. Useabisectionsearch(SeeExercise10.10)to
findtheindexwheretherandomnumberwouldbeinsertedinthecumulativesum.
4. Usetheindextofindthecorrespondingwordinthewordlist.
Exercise13.7. Writeaprogramthatusesthisalgorithmtochoosearandomwordfromthebook.
Solution: https://thinkpython.com/code/analyze_book3.py.
| 13.8 | Markov analysis |     |     |     |     |
| ---- | --------------- | --- | --- | --- | --- |
Ifyouchoosewordsfromthebookatrandom,youcangetasenseofthevocabulary,but
youprobablywon’tgetasentence:

13.8. Markovanalysis 131
this the small regard harriet which knightley's it most things
A series of random words seldom makes sense because there is no relationship between
successivewords. Forexample,inarealsentenceyouwouldexpectanarticlelike“the”to
befollowedbyanadjectiveoranoun,andprobablynotaverboradverb.
OnewaytomeasurethesekindsofrelationshipsisMarkovanalysis,whichcharacterizes,
for a given sequence of words, the probability of the words that might come next. For
example,thesongEric,theHalfaBeebegins:
Halfabee,philosophically,
Must,ipsofacto,halfnotbe.
Buthalfthebeehasgottobe
Visavis,itsentity. D’yousee?
Butcanabeebesaidtobe
Ornottobeanentirebee
Whenhalfthebeeisnotabee
Duetosomeancientinjury?
Inthistext,thephrase“halfthe”isalwaysfollowedbytheword“bee”,butthephrase“the
bee”mightbefollowedbyeither“has”or“is”.
TheresultofMarkovanalysisisamappingfromeachprefix(like“halfthe”and“thebee”)
toallpossiblesuffixes(like“has”and“is”).
Giventhismapping,youcangeneratearandomtextbystartingwithanyprefixandchoos-
ingatrandomfromthepossiblesuffixes. Next,youcancombinetheendoftheprefixand
thenewsuffixtoformthenextprefix,andrepeat.
For example, if you start with the prefix “Half a”, then the next word has to be “bee”,
because the prefix only appears once in the text. The next prefix is “a bee”, so the next
suffixmightbe“philosophically”,“be”or“due”.
Inthisexamplethelengthoftheprefixisalwaystwo,butyoucandoMarkovanalysiswith
anyprefixlength.
Exercise13.8. Markovanalysis:
1. WriteaprogramtoreadatextfromafileandperformMarkovanalysis. Theresultshouldbe
adictionarythatmapsfromprefixestoacollectionofpossiblesuffixes. Thecollectionmight
bealist,tuple,ordictionary;itisuptoyoutomakeanappropriatechoice. Youcantestyour
programwithprefixlengthtwo,butyoushouldwritetheprograminawaythatmakesiteasy
totryotherlengths.
2. AddafunctiontothepreviousprogramtogeneraterandomtextbasedontheMarkovanalysis.
HereisanexamplefromEmmawithprefixlength2:
Hewasveryclever,beitsweetnessorbeangry,ashamedoronlyamused,atsuch
astroke. ShehadneverthoughtofHannahtillyouwerenevermeantforme?""I
cannotmakespeeches,Emma:"hesooncutitallhimself.
Forthisexample,Ileftthepunctuationattachedtothewords. Theresultisalmostsyntacti-
callycorrect,butnotquite. Semantically,italmostmakessense,butnotquite.
Whathappensifyouincreasetheprefixlength? Doestherandomtextmakemoresense?

132 Chapter13. Casestudy: datastructureselection
3. Onceyourprogramisworking,youmightwanttotryamash-up: ifyoucombinetextfrom
twoormorebooks,therandomtextyougeneratewillblendthevocabularyandphrasesfrom
thesourcesininterestingways.
Credit: This case study is based on an example from Kernighan and Pike, The Practice of Pro-
gramming,Addison-Wesley,1999.
You should attempt this exercise before you go on; then you can download my so-
lution from https://thinkpython.com/code/markov.py. You will also need https://
thinkpython.com/code/emma.txt.
13.9 Data structures
Using Markov analysis to generate random text is fun, but there is also a point to this
exercise: data structure selection. In your solution to the previous exercises, you had to
choose:
• Howtorepresenttheprefixes.
• Howtorepresentthecollectionofpossiblesuffixes.
• Howtorepresentthemappingfromeachprefixtothecollectionofpossiblesuffixes.
Thelastoneiseasy: adictionaryistheobviouschoiceforamappingfromkeystocorre-
spondingvalues.
Fortheprefixes,themostobviousoptionsarestring,listofstrings,ortupleofstrings.
Forthesuffixes,oneoptionisalist;anotherisahistogram(dictionary).
How should you choose? The first step is to think about the operations you will need to
implement foreach datastructure. For theprefixes, weneed tobe able toremove words
fromthebeginningandaddtotheend. Forexample,ifthecurrentprefixis“Halfa”,and
thenextwordis“bee”,youneedtobeabletoformthenextprefix,“abee”.
Your first choice might be a list, since it is easy to add and remove elements, but we also
needtobeabletousetheprefixesaskeysinadictionary,sothatrulesoutlists.Withtuples,
youcan’tappendorremove,butyoucanusetheadditionoperatortoformanewtuple:
def shift(prefix, word):
return prefix[1:] + (word,)
shifttakesatupleofwords, prefix, andastring, word, andformsanewtuplethathas
allthewordsinprefixexceptthefirst,andwordaddedtotheend.
For the collection of suffixes, the operations we need to perform include adding a new
suffix(orincreasingthefrequencyofanexistingone),andchoosingarandomsuffix.
Addinganewsuffixisequallyeasyforthelistimplementationorthehistogram.Choosing
arandomelementfromalistiseasy;choosingfromahistogramishardertodoefficiently
(seeExercise13.7).
Sofarwehavebeentalkingmostlyabouteaseofimplementation,butthereareotherfac-
torstoconsiderinchoosingdatastructures. Oneisruntime. Sometimesthereisatheoreti-
calreasontoexpectonedatastructuretobefasterthanother;forexample,Imentionedthat

13.10. Debugging 133
theinoperatorisfasterfordictionariesthanforlists,atleastwhenthenumberofelements
islarge.
Butoftenyoudon’tknowaheadoftimewhichimplementationwillbefaster.Oneoptionis
toimplementbothofthemandseewhichisbetter. Thisapproachiscalledbenchmarking.
Apracticalalternativeistochoosethedatastructurethatiseasiesttoimplement,andthen
seeifitisfastenoughfortheintendedapplication. Ifso,thereisnoneedtogoon. Ifnot,
therearetools,liketheprofilemodule,thatcanidentifytheplacesinaprogramthattake
themosttime.
Theotherfactortoconsiderisstoragespace. Forexample, usingahistogramforthecol-
lectionofsuffixesmighttakelessspacebecauseyouonlyhavetostoreeachwordonce,no
matterhowmanytimesitappearsinthetext. Insomecases, savingspacecanalsomake
yourprogramrunfaster,andintheextreme,yourprogrammightnotrunatallifyourun
out of memory. But for many applications, space is a secondary consideration after run
time.
Onefinalthought: inthisdiscussion,Ihaveimpliedthatweshoulduseonedatastructure
forbothanalysisandgeneration. Butsincetheseareseparatephases,itwouldalsobepos-
sibletouseonestructureforanalysisandthenconverttoanotherstructureforgeneration.
This would be a net win if the time saved during generation exceeded the time spent in
conversion.
13.10 Debugging
When you are debugging a program, and especially if you are working on a hard bug,
therearefivethingstotry:
Reading: Examine your code, read it back to yourself, and check that it says what you
meanttosay.
Running: Experiment by making changes and running different versions. Often if you
displaytherightthingattherightplaceintheprogram,theproblembecomesobvi-
ous,butsometimesyouhavetobuildscaffolding.
Ruminating: Takesometimetothink! Whatkindoferrorisit: syntax,runtime,orseman-
tic? Whatinformationcanyougetfromtheerrormessages,orfromtheoutputofthe
program? Whatkindoferrorcouldcausetheproblemyou’reseeing? Whatdidyou
changelast,beforetheproblemappeared?
Rubberducking: If you explain the problem to someone else, you sometimes find the
answer before you finish asking the question. Often you don’t need the other
person; you could just talk to a rubber duck. And that’s the origin of the well-
known strategy called rubber duck debugging. I am not making this up; see
https://en.wikipedia.org/wiki/Rubber_duck_debugging.
Retreating: Atsomepoint,thebestthingtodoisbackoff,undoingrecentchanges,until
yougetbacktoaprogramthatworksandthatyouunderstand. Thenyoucanstart
rebuilding.

134 Chapter13. Casestudy: datastructureselection
Beginningprogrammerssometimesgetstuckononeoftheseactivitiesandforgettheoth-
ers. Eachactivitycomeswithitsownfailuremode.
For example, reading your code might help if the problem is a typographical error, but
notiftheproblemisaconceptualmisunderstanding. Ifyoudon’tunderstandwhatyour
program does, you can read it 100 times and never see the error, because the error is in
yourhead.
Running experiments can help, especially if you run small, simple tests. But if you run
experiments without thinking or reading your code, you might fall into a pattern I call
“random walk programming”, which is the process of making random changes until the
programdoestherightthing. Needlesstosay,randomwalkprogrammingcantakealong
time.
Youhavetotaketimetothink.Debuggingislikeanexperimentalscience.Youshouldhave
atleastonehypothesisaboutwhattheproblemis. Iftherearetwoormorepossibilities,try
tothinkofatestthatwouldeliminateoneofthem.
Buteventhebestdebuggingtechniqueswillfailiftherearetoomanyerrors,orifthecode
you are trying to fix is too big and complicated. Sometimes the best option is to retreat,
simplifyingtheprogramuntilyougettosomethingthatworksandthatyouunderstand.
Beginningprogrammersareoftenreluctanttoretreatbecausetheycan’tstandtodeletea
lineofcode(evenifit’swrong).Ifitmakesyoufeelbetter,copyyourprogramintoanother
filebeforeyoustartstrippingitdown. Thenyoucancopythepiecesbackoneatatime.
Finding a hard bug requires reading, running, ruminating, and sometimes retreating. If
yougetstuckononeoftheseactivities,trytheothers.
13.11 Glossary
deterministic: Pertaining to a program that does the same thing each time it runs, given
thesameinputs.
pseudorandom: Pertaining to a sequence of numbers that appears to be random, but is
generatedbyadeterministicprogram.
defaultvalue: Thevaluegiventoanoptionalparameterifnoargumentisprovided.
override: Toreplaceadefaultvaluewithanargument.
benchmarking: The process of choosing between data structures by implementing alter-
nativesandtestingthemonasampleofthepossibleinputs.
rubberduckdebugging: Debugging by explaining your problem to an inanimate object
such as a rubber duck. Articulating the problem can help you solve it, even if the
rubberduckdoesn’tknowPython.
13.12 Exercises
Exercise13.9. The“rank”ofawordisitspositioninalistofwordssortedbyfrequency: themost
commonwordhasrank1,thesecondmostcommonhasrank2,etc.

13.12. Exercises 135
Zipf’slawdescribesarelationshipbetweentheranksandfrequenciesofwordsinnaturallanguages
(http://en.wikipedia.org/wiki/Zipf’s_law).Specifically,itpredictsthatthefrequency,
f,ofthewordwithrankris:
f = cr −s
wheresandcareparametersthatdependonthelanguageandthetext. Ifyoutakethelogarithmof
bothsidesofthisequation,youget:
log f =logc−slogr
Soifyouplotlog f versuslogr,youshouldgetastraightlinewithslope−sandinterceptlogc.
Writeaprogramthatreadsatextfromafile,countswordfrequencies,andprintsonelineforeach
word, in descending order of frequency, with log f and log r. Use the graphing program of your
choicetoplottheresultsandcheckwhethertheyformastraightline. Canyouestimatethevalueof
s?
Solution:https://thinkpython.com/code/zipf.py.Torunmysolution,youneedtheplot-
tingmodulematplotlib.IfyouinstalledAnaconda,youalreadyhavematplotlib;otherwiseyou
mighthavetoinstallit.

| 136 | Chapter13. | Casestudy: | datastructureselection |
| --- | ---------- | ---------- | ---------------------- |

Chapter 14
Files
Thischapterintroducestheideaof“persistent”programsthatkeepdatainpermanentstor-
age,andshowshowtousedifferentkindsofpermanentstorage,likefilesanddatabases.
14.1 Persistence
Mostoftheprogramswehaveseensofararetransientinthesensethattheyrunforashort
timeandproducesomeoutput, butwhentheyend, theirdatadisappears. Ifyourunthe
programagain,itstartswithacleanslate.
Otherprogramsarepersistent: theyrunforalongtime(orallthetime);theykeepatleast
someoftheirdatainpermanentstorage(aharddrive,forexample);andiftheyshutdown
andrestart,theypickupwheretheyleftoff.
Examplesofpersistentprogramsareoperatingsystems,whichrunprettymuchwhenever
acomputerison,andwebservers,whichrunallthetime,waitingforrequeststocomein
onthenetwork.
One of the simplest ways for programs to maintain their data is by reading and writing
text files. We have already seen programs that read text files; in this chapter we will see
programsthatwritethem.
Analternativeistostorethestateoftheprograminadatabase.InthischapterIwillpresent
asimpledatabaseandamodule,pickle,thatmakesiteasytostoreprogramdata.
14.2 Reading and writing
A text file is a sequence of characters stored on a permanent medium like a hard drive,
flashmemory,orCD-ROM.WesawhowtoopenandreadafileinSection9.1.
Towriteafile,youhavetoopenitwithmode'w'asasecondparameter:
>>> fout = open('output.txt', 'w')

| 138 |     |     |     |     | Chapter14. | Files |
| --- | --- | --- | --- | --- | ---------- | ----- |
Ifthefilealreadyexists, openingitinwritemodeclearsouttheolddataandstartsfresh,
| sobecareful! | Ifthefiledoesn’texist,anewoneiscreated. |     |     |     |     |     |
| ------------ | --------------------------------------- | --- | --- | --- | --- | --- |
open returns a file object that provides methods for working with the file. The write
methodputsdataintothefile.
| >>> line1 | = "This here's | the wattle,\n" |     |     |     |     |
| --------- | -------------- | -------------- | --- | --- | --- | --- |
>>> fout.write(line1)
24
Thereturnvalueisthenumberofcharactersthatwerewritten. Thefileobjectkeepstrack
ofwhereitis,soifyoucallwriteagain,itaddsthenewdatatotheendofthefile.
| >>> line2 | = "the emblem | of our | land.\n" |     |     |     |
| --------- | ------------- | ------ | -------- | --- | --- | --- |
>>> fout.write(line2)
24
Whenyouaredonewriting,youshouldclosethefile.
>>> fout.close()
Ifyoudon’tclosethefile,itgetsclosedforyouwhentheprogramends.
| 14.3 | Format operator |     |     |     |     |     |
| ---- | --------------- | --- | --- | --- | --- | --- |
write
The argument of has to be a string, so if we want to put other values in a file, we
| havetoconvertthemtostrings. |     | Theeasiestwaytodothatiswithstr: |     |     |     |     |
| --------------------------- | --- | ------------------------------- | --- | --- | --- | --- |
| >>> x =                     | 52  |                                 |     |     |     |     |
>>> fout.write(str(x))
Analternativeistousetheformatoperator,%. Whenappliedtointegers,%isthemodulus
Butwhenthefirstoperandisastring,%istheformatoperator.
operator.
The first operand is the format string, which contains one or more format sequences,
| whichspecifyhowthesecondoperandisformatted. |     |     |     | Theresultisastring. |     |     |
| ------------------------------------------- | --- | --- | --- | ------------------- | --- | --- |
Forexample,theformatsequence'%d'meansthatthesecondoperandshouldbeformat-
tedasadecimalinteger:
| >>> camels | = 42     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
| >>> '%d'   | % camels |     |     |     |     |     |
'42'
Theresultisthestring'42',whichisnottobeconfusedwiththeintegervalue42.
A format sequence can appear anywhere in the string, so you can embed a value in a
sentence:
| >>> 'I  | have spotted        | %d camels.' | % camels |     |     |     |
| ------- | ------------------- | ----------- | -------- | --- | --- | --- |
| 'I have | spotted 42 camels.' |             |          |     |     |     |
If there is more than one format sequence in the string, the second argument has to be a
tuple. Eachformatsequenceismatchedwithanelementofthetuple,inorder.
Thefollowingexampleuses'%d'toformataninteger,'%g'toformatafloating-pointnum-
ber,and'%s'toformatastring:
| >>> 'In     | %d years I have | spotted | %g %s.' % (3, | 0.1, 'camels') |     |     |
| ----------- | --------------- | ------- | ------------- | -------------- | --- | --- |
| 'In 3 years | I have spotted  | 0.1     | camels.'      |                |     |     |

| 14.4. Filenamesandpaths |     |     |     |     |     | 139 |
| ----------------------- | --- | --- | --- | --- | --- | --- |
Thenumberofelementsinthetuplehastomatchthenumberofformatsequencesinthe
string. Also,thetypesoftheelementshavetomatchtheformatsequences:
| >>> '%d    | %d %d' % (1, | 2)        |              |         |     |     |
| ---------- | ------------ | --------- | ------------ | ------- | --- | --- |
| TypeError: | not enough   | arguments | for format   | string  |     |     |
| >>> '%d'   | % 'dollars'  |           |              |         |     |     |
| TypeError: | %d format:   | a number  | is required, | not str |     |     |
Inthefirstexample,therearen’tenoughelements;inthesecond,theelementisthewrong
type.
Formoreinformationontheformatoperator,seehttps://docs.python.org/3/library/
stdtypes.html#printf-style-string-formatting.
|     |     |     |     | A more powerful | alternative | is  |
| --- | --- | --- | --- | --------------- | ----------- | --- |
the string format method, which you can read about at https://docs.python.org/3/
library/stdtypes.html#str.format.
| 14.4 | Filenames | and paths |     |     |     |     |
| ---- | --------- | --------- | --- | --- | --- | --- |
Files are organized into directories (also called “folders”). Every running program has a
“currentdirectory”,whichisthedefaultdirectoryformostoperations. Forexample,when
youopenafileforreading,Pythonlooksforitinthecurrentdirectory.
os
The module providesfunctions forworking with filesand directories(“os” stands for
| “operatingsystem”). |               | os.getcwdreturnsthenameofthecurrentdirectory: |     |     |     |     |
| ------------------- | ------------- | --------------------------------------------- | --- | --- | --- | --- |
| >>> import          | os            |                                               |     |     |     |     |
| >>> cwd             | = os.getcwd() |                                               |     |     |     |     |
>>> cwd
'/home/dinsdale'
cwdstandsfor“currentworkingdirectory”. Theresultinthisexampleis/home/dinsdale,
whichisthehomedirectoryofausernameddinsdale.
Astringlike'/home/dinsdale'thatidentifiesafileordirectoryiscalledapath.
Asimplefilename,likememo.txtisalsoconsideredapath,butitisarelativepathbecause
Ifthecurrentdirectoryis/home/dinsdale,thefilename
itrelatestothecurrentdirectory.
memo.txtwouldreferto/home/dinsdale/memo.txt.
Apaththatbeginswith/doesnotdependonthecurrentdirectory;itiscalledanabsolute
Tofindtheabsolutepathtoafile,youcanuseos.path.abspath:
path.
>>> os.path.abspath('memo.txt')
'/home/dinsdale/memo.txt'
os.path provides other functions for working with filenames and paths. For example,
os.path.existscheckswhetherafileordirectoryexists:
>>> os.path.exists('memo.txt')
True
Ifitexists,os.path.isdircheckswhetherit’sadirectory:
>>> os.path.isdir('memo.txt')
False
>>> os.path.isdir('/home/dinsdale')
True

| 140 |     |     |     |     | Chapter14. | Files |
| --- | --- | --- | --- | --- | ---------- | ----- |
Similarly,os.path.isfilecheckswhetherit’safile.
os.listdirreturnsalistofthefiles(andotherdirectories)inthegivendirectory:
>>> os.listdir(cwd)
| ['music', | 'photos', | 'memo.txt'] |     |     |     |     |
| --------- | --------- | ----------- | --- | --- | --- | --- |
Todemonstratethesefunctions,thefollowingexample“walks”throughadirectory,prints
thenamesofallthefiles,andcallsitselfrecursivelyonallthedirectories.
def walk(dirname):
| for | name in                      | os.listdir(dirname): |     |       |     |     |
| --- | ---------------------------- | -------------------- | --- | ----- | --- | --- |
|     | path = os.path.join(dirname, |                      |     | name) |     |     |
if os.path.isfile(path):
print(path)
else:
walk(path)
os.path.jointakesadirectoryandafilenameandjoinsthemintoacompletepath.
| os  |     |     |     | walk |     |     |
| --- | --- | --- | --- | ---- | --- | --- |
The module provides a function called that is similar to this one but more ver-
satile. As an exercise, read the documentation and use it to print the names of the
files in a given directory and its subdirectories. You can download my solution from
https://thinkpython.com/code/walk.py.
| 14.5 | Catching | exceptions |     |     |     |     |
| ---- | -------- | ---------- | --- | --- | --- | --- |
Alotofthingscangowrongwhenyoutrytoreadandwritefiles. Ifyoutrytoopenafile
thatdoesn’texist,yougetanFileNotFoundError:
| >>> fin | = open('bad_file') |     |     |     |     |     |
| ------- | ------------------ | --- | --- | --- | --- | --- |
FileNotFoundError: [Errno 2] No such file or directory: 'bad_file'
Ifyoudon’thavepermissiontoaccessafile:
| >>> fout         | = open('/etc/passwd', |            | 'w')       |                       |     |     |
| ---------------- | --------------------- | ---------- | ---------- | --------------------- | --- | --- |
| PermissionError: |                       | [Errno 13] | Permission | denied: '/etc/passwd' |     |     |
Andifyoutrytoopenadirectoryforreading,youget
| >>> fin            | = open('/home') |        |                     |         |     |     |
| ------------------ | --------------- | ------ | ------------------- | ------- | --- | --- |
| IsADirectoryError: |                 | [Errno | 21] Is a directory: | '/home' |     |     |
Toavoidtheseerrors,youcouldusefunctionslikeos.path.existsandos.path.isfile,
butitwouldtakealotoftimeandcodetocheckallthepossibilities(if“Errno 21”isany
indication,thereareatleast21thingsthatcangowrong).
Itisbettertogoaheadandtry—anddealwithproblemsiftheyhappen—whichisexactly
whatthetrystatementdoes. Thesyntaxissimilartoanif...elsestatement:
try:
| fin | = open('bad_file') |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
except:
| print('Something |     | went | wrong.') |     |     |     |
| ---------------- | --- | ---- | -------- | --- | --- | --- |

14.6. Databases 141
Python starts by executing the try clause. If all goes well, it skips the except clause and
proceeds. Ifanexceptionoccurs,itjumpsoutofthetryclauseandrunstheexceptclause.
Handlinganexceptionwithatrystatementiscalledcatchinganexception. Inthisexam-
ple,theexceptclauseprintsanerrormessagethatisnotveryhelpful. Ingeneral,catching
anexceptiongivesyouachancetofixtheproblem,ortryagain,oratleastendtheprogram
gracefully.
14.6 Databases
Adatabaseisafilethatisorganizedforstoringdata. Manydatabasesareorganizedlikea
dictionaryinthesensethattheymapfromkeystovalues. Thebiggestdifferencebetween
adatabaseandadictionaryisthatthedatabaseisondisk(orotherpermanentstorage),so
itpersistsaftertheprogramends.
The module dbm provides an interface for creating and updating database files. As an
example,I’llcreateadatabasethatcontainscaptionsforimagefiles.
Openingadatabaseissimilartoopeningotherfiles:
>>> import dbm
>>> db = dbm.open('captions', 'c')
The mode 'c' means that the database should be created if it doesn’t already exist. The
resultisadatabaseobjectthatcanbeused(formostoperations)likeadictionary.
Whenyoucreateanewitem,dbmupdatesthedatabasefile.
>>> db['cleese.png'] = 'Photo of John Cleese.'
Whenyouaccessoneoftheitems,dbmreadsthefile:
>>> db['cleese.png']
b'Photo of John Cleese.'
The result is a bytes object, which is why it begins with b. A bytes object is similar to a
stringinmanyways. WhenyougetfartherintoPython,thedifferencebecomesimportant,
butfornowwecanignoreit.
Ifyoumakeanotherassignmenttoanexistingkey,dbmreplacestheoldvalue:
>>> db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
>>> db['cleese.png']
b'Photo of John Cleese doing a silly walk.'
Some dictionary methods, like keys and items, don’t work with database objects. But
iterationwithaforloopworks:
for key in db.keys():
print(key, db[key])
Aswithotherfiles,youshouldclosethedatabasewhenyouaredone:
>>> db.close()

142 Chapter14. Files
14.7 Pickling
Alimitationofdbmisthatthekeysandvalueshavetobestringsorbytes. Ifyoutrytouse
anyothertype,yougetanerror.
Thepicklemodulecanhelp. Ittranslatesalmostanytypeofobjectintoastringsuitable
forstorageinadatabase,andthentranslatesstringsbackintoobjects.
pickle.dumpstakesanobjectasaparameterandreturnsastringrepresentation(dumpsis
shortfor“dumpstring”):
>>> import pickle
>>> t = [1, 2, 3]
>>> pickle.dumps(t)
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
Theformatisn’tobvioustohumanreaders; itismeanttobeeasyforpickletointerpret.
pickle.loads(“loadstring”)reconstitutestheobject:
>>> t1 = [1, 2, 3]
>>> s = pickle.dumps(t1)
>>> t2 = pickle.loads(s)
>>> t2
[1, 2, 3]
Althoughthenewobjecthasthesamevalueastheold,itisnot(ingeneral)thesameobject:
>>> t1 == t2
True
>>> t1 is t2
False
Inotherwords,picklingandthenunpicklinghasthesameeffectascopyingtheobject.
Youcanusepickletostorenon-stringsinadatabase. Infact,thiscombinationissocom-
monthatithasbeenencapsulatedinamodulecalledshelve.
14.8 Pipes
Most operating systems provide a command-line interface, also known as a shell. Shells
usuallyprovidecommandstonavigatethefilesystemandlaunchapplications. Forexam-
ple,inUnixyoucanchangedirectorieswithcd,displaythecontentsofadirectorywithls,
andlaunchawebbrowserbytyping(forexample)firefox.
AnyprogramthatyoucanlaunchfromtheshellcanalsobelaunchedfromPythonusing
apipeobject,whichrepresentsarunningprogram.
For example, the Unix command ls -l normally displays the contents of the current di-
rectoryinlongformat. Youcanlaunchlswithos.popen1:
>>> cmd = 'ls -l'
>>> fp = os.popen(cmd)
1popenisdeprecatednow, whichmeanswearesupposedtostopusingitandstartusingthesubprocess
module. Butforsimplecases,Ifindsubprocessmorecomplicatedthannecessary. SoIamgoingtokeepusing
popenuntiltheytakeitaway.

14.9. Writingmodules 143
Theargumentisastringthatcontainsashellcommand. Thereturnvalueisanobjectthat
behaves like an open file. You can read the output from the ls process one line at a time
withreadlineorgetthewholethingatoncewithread:
| >>> res | = fp.read() |     |
| ------- | ----------- | --- |
Whenyouaredone,youclosethepipelikeafile:
| >>> stat | = fp.close() |     |
| -------- | ------------ | --- |
>>> print(stat)
None
ls None
The return value is the final status of the process; means that it ended normally
(withnoerrors).
Forexample,mostUnixsystemsprovideacommandcalledmd5sumthatreadsthecontents
YoucanreadaboutMD5athttp://en.wikipedia.
ofafileandcomputesa“checksum”.
org/wiki/Md5. Thiscommandprovidesanefficientwaytocheckwhethertwofileshave
thesamecontents. Theprobabilitythatdifferentcontentsyieldthesamechecksumisvery
small(thatis,unlikelytohappenbeforetheuniversecollapses).
Youcanuseapipetorunmd5sumfromPythonandgettheresult:
| >>> filename | = 'book.tex'    |              |
| ------------ | --------------- | ------------ |
| >>> cmd      | = 'md5sum       | ' + filename |
| >>> fp       | = os.popen(cmd) |              |
| >>> res      | = fp.read()     |              |
| >>> stat     | = fp.close()    |              |
>>> print(res)
1e0033f0ed0656636de0d75144ba32e0 book.tex
>>> print(stat)
None
| 14.9 | Writing | modules |
| ---- | ------- | ------- |
Any file that contains Python code can be imported as a module. For example, suppose
youhaveafilenamedwc.pywiththefollowingcode:
def linecount(filename):
| count | = 0                     |     |
| ----- | ----------------------- | --- |
| for   | line in open(filename): |     |
count += 1
| return | count |     |
| ------ | ----- | --- |
print(linecount('wc.py'))
Ifyourunthisprogram,itreadsitselfandprintsthenumberoflinesinthefile,whichis7.
Youcanalsoimportitlikethis:
| >>> import | wc  |     |
| ---------- | --- | --- |
7
Nowyouhaveamoduleobjectwc:
>>> wc
| <module | 'wc' from | 'wc.py'> |
| ------- | --------- | -------- |

144 Chapter14. Files
Themoduleobjectprovideslinecount:
>>> wc.linecount('wc.py')
7
Sothat’showyouwritemodulesinPython.
The only problem with this example is that when you import the module it runs the test
codeatthebottom. Normallywhenyouimportamodule,itdefinesnewfunctionsbutit
doesn’trunthem.
Programsthatwillbeimportedasmodulesoftenusethefollowingidiom:
if __name__ == '__main__':
print(linecount('wc.py'))
__name__isabuilt-invariablethatissetwhentheprogramstarts.Iftheprogramisrunning
asascript,__name__hasthevalue'__main__';inthatcase,thetestcoderuns. Otherwise,
ifthemoduleisbeingimported,thetestcodeisskipped.
Asanexercise,typethisexampleintoafilenamedwc.pyandrunitasascript. Thenrun
thePythoninterpreterandimport wc. Whatisthevalueof__name__whenthemoduleis
beingimported?
Warning: Ifyouimportamodulethathasalreadybeenimported,Pythondoesnothing. It
doesnotre-readthefile,evenifithaschanged.
If you want to reload a module, you can use the built-in function reload, but it can be
tricky,sothesafestthingtodoisrestarttheinterpreterandthenimportthemoduleagain.
14.10 Debugging
When you are reading and writing files, you might run into problems with whitespace.
Theseerrorscanbehardtodebugbecausespaces,tabsandnewlinesarenormallyinvisible:
>>> s = '1 2\t 3\n 4'
>>> print(s)
1 2 3
4
Thebuilt-infunctionreprcanhelp. Ittakesanyobjectasanargumentandreturnsastring
representationoftheobject. Forstrings,itrepresentswhitespacecharacterswithbackslash
sequences:
>>> print(repr(s))
'1 2\t 3\n 4'
Thiscanbehelpfulfordebugging.
Oneotherproblemyoumightrunintoisthatdifferentsystemsusedifferentcharactersto
indicatetheendofaline. Somesystemsuseanewline,represented\n. Othersuseareturn
character, represented \r. Some use both. If you move files between different systems,
theseinconsistenciescancauseproblems.
For most systems, there are applications to convert from one format to another. You can
find them (and read more about this issue) at http://en.wikipedia.org/wiki/Newline.
Or,ofcourse,youcouldwriteoneyourself.

14.11. Glossary 145
14.11 Glossary
persistent: Pertaining to a program that runs indefinitely and keeps at least some of its
datainpermanentstorage.
formatoperator: An operator, %, that takes a format string and a tuple and generates a
string that includes the elements of the tuple formatted as specified by the format
string.
formatstring: Astring,usedwiththeformatoperator,thatcontainsformatsequences.
formatsequence: Asequenceofcharactersinaformatstring,like%d,thatspecifieshowa
valueshouldbeformatted.
textfile: Asequenceofcharactersstoredinpermanentstoragelikeaharddrive.
directory: Anamedcollectionoffiles,alsocalledafolder.
path: Astringthatidentifiesafile.
relativepath: Apaththatstartsfromthecurrentdirectory.
absolutepath: Apaththatstartsfromthetopmostdirectoryinthefilesystem.
catch: Topreventanexceptionfromterminatingaprogramusingthetryandexceptstate-
ments.
database: Afilewhosecontentsareorganizedlikeadictionarywithkeysthatcorrespond
tovalues.
bytesobject: Anobjectsimilartoastring.
shell: Aprogramthatallowsuserstotypecommandsandthenexecutesthembystarting
otherprograms.
pipeobject: Anobjectthatrepresentsarunningprogram,allowingaPythonprogramto
runcommandsandreadtheresults.
14.12 Exercises
Exercise14.1. Writeafunctioncalledsedthattakesasargumentsapatternstring,areplacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
withthereplacementstring.
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception,printanerrormessage,andexit.Solution:https://thinkpython.com/code/sed.
py.
Exercise14.2. IfyoudownloadmysolutiontoExercise12.2fromhttps://thinkpython.com/
code/anagram_sets.py,you’llseethatitcreatesadictionarythatmapsfromasortedstringof
letterstothelistofwordsthatcanbespelledwiththoseletters. Forexample, 'opst'mapstothe
list['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
Write a module that imports anagram_sets and provides two new functions: store_anagrams
shouldstoretheanagramdictionaryina“shelf”;read_anagramsshouldlookupawordandreturn
alistofitsanagrams. Solution: https://thinkpython.com/code/anagram_db.py.

146 Chapter14. Files
Exercise14.3. InalargecollectionofMP3files,theremaybemorethanonecopyofthesamesong,
stored in different directories or with different file names. The goal of this exercise is to search for
duplicates.
1. Writeaprogramthatsearchesadirectoryandallofitssubdirectories,recursively,andreturns
alistofcompletepathsforallfileswithagivensuffix(like.mp3). Hint: os.pathprovides
severalusefulfunctionsformanipulatingfileandpathnames.
2. Torecognizeduplicates, youcanusemd5sumtocomputea“checksum”foreachfiles. Iftwo
fileshavethesamechecksum,theyprobablyhavethesamecontents.
3. Todouble-check,youcanusetheUnixcommanddiff.
Solution: https://thinkpython.com/code/find_duplicates.py.

Chapter 15
Classes and objects
Atthispointyouknowhowtousefunctionstoorganizecodeandbuilt-intypestoorganize
data. The next step is to learn “object-oriented programming”, which uses programmer-
definedtypestoorganizebothcodeanddata. Object-orientedprogrammingisabigtopic;
itwilltakeafewchapterstogetthere.
Code examples from this chapter are available from https://thinkpython.com/code/
Point1.py;solutionstotheexercisesareavailablefromhttps://thinkpython.com/code/
Point1_soln.py.
15.1 Programmer-defined types
WehaveusedmanyofPython’sbuilt-intypes;nowwearegoingtodefineanewtype. As
anexample,wewillcreateatypecalledPointthatrepresentsapointintwo-dimensional
space.
Inmathematicalnotation,pointsareoftenwritteninparentheseswithacommaseparating
thecoordinates. Forexample,(0,0)representstheorigin,and(x,y)representsthepointx
unitstotherightandyunitsupfromtheorigin.
ThereareseveralwayswemightrepresentpointsinPython:
• Wecouldstorethecoordinatesseparatelyintwovariables,xandy.
• Wecouldstorethecoordinatesaselementsinalistortuple.
• Wecouldcreateanewtypetorepresentpointsasobjects.
Creatinganewtypeismorecomplicatedthantheotheroptions,butithasadvantagesthat
willbeapparentsoon.
Aprogrammer-definedtypeisalsocalledaclass. Aclassdefinitionlookslikethis:
class Point:
"""Represents a point in 2-D space."""

148 Chapter15. Classesandobjects
Point
blank x 3.0
y 4.0
Figure15.1: Objectdiagram.
The header indicates that the new class is called Point. The body is a docstring that ex-
plainswhattheclassisfor. Youcandefinevariablesandmethodsinsideaclassdefinition,
butwewillgetbacktothatlater.
DefiningaclassnamedPointcreatesaclassobject.
>>> Point
<class '__main__.Point'>
BecausePointisdefinedatthetoplevel,its“fullname”is__main__.Point.
Theclassobjectislikeafactoryforcreatingobjects. TocreateaPoint,youcallPointasifit
wereafunction.
>>> blank = Point()
>>> blank
<__main__.Point object at 0xb7e9d3ac>
ThereturnvalueisareferencetoaPointobject,whichweassigntoblank.
Creatinganewobjectiscalledinstantiation,andtheobjectisaninstanceoftheclass.
Whenyouprintaninstance,Pythontellsyouwhatclassitbelongstoandwhereitisstored
inmemory(theprefix0xmeansthatthefollowingnumberisinhexadecimal).
Every object is an instance of some class, so “object” and “instance” are interchangeable.
But in this chapter I use “instance” to indicate that I am talking about a programmer-
definedtype.
15.2 Attributes
Youcanassignvaluestoaninstanceusingdotnotation:
>>> blank.x = 3.0
>>> blank.y = 4.0
Thissyntaxissimilartothesyntaxforselectingavariablefromamodule,suchasmath.pi
orstring.whitespace. Inthiscase,though,weareassigningvaluestonamedelementsof
anobject. Theseelementsarecalledattributes.
Asanoun,“AT-trib-ute”ispronouncedwithemphasisonthefirstsyllable,asopposedto
“a-TRIB-ute”,whichisaverb.
Figure15.1isastatediagramthatshowstheresultoftheseassignments. Astatediagram
thatshowsanobjectanditsattributesiscalledanobjectdiagram.
The variable blank refers to a Point object, which contains two attributes. Each attribute
referstoafloating-pointnumber.
Youcanreadthevalueofanattributeusingthesamesyntax:

15.3. Rectangles 149
>>> blank.y
4.0
>>> x = blank.x
>>> x
3.0
Theexpressionblank.xmeans,“Gototheobjectblankreferstoandgetthevalueofx.” In
theexample,weassignthatvaluetoavariablenamedx. Thereisnoconflictbetweenthe
variablexandtheattributex.
Youcanusedotnotationaspartofanyexpression. Forexample:
>>> '(%g, %g)' % (blank.x, blank.y)
'(3.0, 4.0)'
>>> distance = math.sqrt(blank.x**2 + blank.y**2)
>>> distance
5.0
Youcanpassaninstanceasanargumentintheusualway. Forexample:
def print_point(p):
print('(%g, %g)' % (p.x, p.y))
print_point takes a point as an argument and displays it in mathematical notation. To
invokeit,youcanpassblankasanargument:
>>> print_point(blank)
(3.0, 4.0)
Insidethefunction,pisanaliasforblank,soifthefunctionmodifiesp,blankchanges.
Asanexercise,writeafunctioncalleddistance_between_pointsthattakestwoPointsas
argumentsandreturnsthedistancebetweenthem.
15.3 Rectangles
Sometimesitisobviouswhattheattributesofanobjectshouldbe,butothertimesyouhave
tomakedecisions. Forexample,imagineyouaredesigningaclasstorepresentrectangles.
Whatattributeswouldyouusetospecifythelocationandsizeofarectangle? Youcanig-
noreangle;tokeepthingssimple,assumethattherectangleiseitherverticalorhorizontal.
Thereareatleasttwopossibilities:
• You could specify one corner of the rectangle (or the center), the width, and the
height.
• Youcouldspecifytwoopposingcorners.
Atthispointitishardtosaywhethereitherisbetterthantheother,sowe’llimplementthe
firstone,justasanexample.
Hereistheclassdefinition:

| 150 |     |     | Chapter15. | Classesandobjects |
| --- | --- | --- | ---------- | ----------------- |
Rectangle
|     | box | width 100.0 |     |     |
| --- | --- | ----------- | --- | --- |
Point
height 200.0
x 0.0
corner
y 0.0
Figure15.2: Objectdiagram.
class Rectangle:
| """Represents | a rectangle.   |         |     |     |
| ------------- | -------------- | ------- | --- | --- |
| attributes:   | width, height, | corner. |     |     |
"""
widthandheightarenumbers;cornerisaPointobject
Thedocstringliststheattributes:
thatspecifiesthelower-leftcorner.
Torepresentarectangle,youhavetoinstantiateaRectangleobjectandassignvaluestothe
attributes:
box = Rectangle()
| box.width = 100.0 |         |     |     |     |
| ----------------- | ------- | --- | --- | --- |
| box.height =      | 200.0   |     |     |     |
| box.corner =      | Point() |     |     |     |
| box.corner.x      | = 0.0   |     |     |     |
| box.corner.y      | = 0.0   |     |     |     |
Theexpressionbox.corner.xmeans,“Gototheobjectboxreferstoandselecttheattribute
namedcorner;thengotothatobjectandselecttheattributenamedx.”
Figure15.2showsthestateofthisobject. Anobjectthatisanattributeofanotherobjectis
embedded.
| 15.4 Instances | as return | values |     |     |
| -------------- | --------- | ------ | --- | --- |
Functionscanreturninstances. Forexample, find_centertakesaRectangleasanargu-
mentandreturnsaPointthatcontainsthecoordinatesofthecenteroftheRectangle:
def find_center(rect):
p = Point()
| p.x = rect.corner.x | + rect.width/2  |     |     |     |
| ------------------- | --------------- | --- | --- | --- |
| p.y = rect.corner.y | + rect.height/2 |     |     |     |
| return p            |                 |     |     |     |
box
Here is an example that passes as an argument and assigns the resulting Point to
center:
| >>> center = | find_center(box) |     |     |     |
| ------------ | ---------------- | --- | --- | --- |
>>> print_point(center)
(50, 100)

15.5. Objectsaremutable 151
| 15.5 | Objects are | mutable |
| ---- | ----------- | ------- |
Youcanchangethestateofanobjectbymakinganassignmenttooneofitsattributes. For
example, to change the size of a rectangle without changing its position, you can modify
thevaluesofwidthandheight:
| box.width  | = box.width  | + 50  |
| ---------- | ------------ | ----- |
| box.height | = box.height | + 100 |
You can also write functions that modify objects. For example, grow_rectangle takes a
dwidth dheight,
Rectangle object and two numbers, and and adds the numbers to the
widthandheightoftherectangle:
| def grow_rectangle(rect, |           | dwidth, dheight): |
| ------------------------ | --------- | ----------------- |
| rect.width               | += dwidth |                   |
| rect.height              | +=        | dheight           |
Hereisanexamplethatdemonstratestheeffect:
| >>> box.width,          | box.height |          |
| ----------------------- | ---------- | -------- |
| (150.0,                 | 300.0)     |          |
| >>> grow_rectangle(box, |            | 50, 100) |
| >>> box.width,          | box.height |          |
| (200.0,                 | 400.0)     |          |
Inside the function, rect is an alias for box, so when the function modifies rect, box
changes.
move_rectangle
As an exercise, write a function named that takes a Rectangle and two
numbersnameddxanddy. Itshouldchangethelocationoftherectanglebyaddingdxto
thexcoordinateofcornerandaddingdytotheycoordinateofcorner.
15.6 Copying
Aliasing can make a program difficult to read because changes in one place might have
unexpectedeffectsinanotherplace. Itishardtokeeptrackofallthevariablesthatmight
refertoagivenobject.
Thecopymodulecontainsafunction
Copyinganobjectisoftenanalternativetoaliasing.
calledcopythatcanduplicateanyobject:
| >>> p1     | = Point()       |     |
| ---------- | --------------- | --- |
| >>> p1.x   | = 3.0           |     |
| >>> p1.y   | = 4.0           |     |
| >>> import | copy            |     |
| >>> p2     | = copy.copy(p1) |     |
p1andp2containthesamedata,buttheyarenotthesamePoint.
>>> print_point(p1)
(3, 4)
>>> print_point(p2)
(3, 4)
| >>> p1 | is p2 |     |
| ------ | ----- | --- |
False

| 152 |           |       | Chapter15.   | Classesandobjects |
| --- | --------- | ----- | ------------ | ----------------- |
|     | box width | 100.0 | 100.0 width  | box2              |
|     | height    | 200.0 | 200.0 height |                   |
|     |           | x 0.0 |              |                   |
|     | corner    |       | corner       |                   |
|     |           | y 0.0 |              |                   |
Figure15.3: Objectdiagram.
| >>> p1 | == p2 |     |     |     |
| ------ | ----- | --- | --- | --- |
False
| is  |     | p1 p2 |     |     |
| --- | --- | ----- | --- | --- |
The operator indicates that and are not the same object, which is what we ex-
pected. But you might have expected == to yield True because these points contain the
same data. In that case, you will be disappointed to learn that for instances, the default
behavior of the == operator is the same as the is operator; it checks object identity, not
object equivalence. That’s because for programmer-defined types, Python doesn’t know
| whatshouldbeconsideredequivalent. |     | Atleast,notyet. |     |     |
| --------------------------------- | --- | --------------- | --- | --- |
If you use copy.copy to duplicate a Rectangle, you will find that it copies the Rectangle
objectbutnottheembeddedPoint.
| >>> box2 | = copy.copy(box) |     |     |     |
| -------- | ---------------- | --- | --- | --- |
| >>> box2 | is box           |     |     |     |
False
| >>> box2.corner | is box.corner |     |     |     |
| --------------- | ------------- | --- | --- | --- |
True
Figure15.3showswhattheobjectdiagramlookslike. Thisoperationiscalledashallow
copy because it copies the object and any references it contains, but not the embedded
objects.
For most applications, this is not what you want. In this example, invoking
grow_rectangle on one of the Rectangles would not affect the other, but invoking
move_rectangleoneitherwouldaffectboth!
Thisbehaviorisconfusinganderror-prone.
Fortunately,thecopymoduleprovidesamethodnameddeepcopythatcopiesnotonlythe
objectbutalsotheobjectsitrefersto,andtheobjectstheyreferto,andsoon. Youwillnot
besurprisedtolearnthatthisoperationiscalledadeepcopy.
| >>> box3 | = copy.deepcopy(box) |     |     |     |
| -------- | -------------------- | --- | --- | --- |
| >>> box3 | is box               |     |     |     |
False
| >>> box3.corner | is box.corner |     |     |     |
| --------------- | ------------- | --- | --- | --- |
False
box3andboxarecompletelyseparateobjects.
Asanexercise,writeaversionofmove_rectanglethatcreatesandreturnsanewRectangle
insteadofmodifyingtheoldone.
15.7 Debugging
Whenyoustartworkingwithobjects,youarelikelytoencountersomenewexceptions. If
youtrytoaccessanattributethatdoesn’texist,yougetanAttributeError:

15.8. Glossary 153
>>> p = Point()
| >>> p.x = 3 |     |     |     |
| ----------- | --- | --- | --- |
| >>> p.y = 4 |     |     |     |
>>> p.z
| AttributeError: | Point instance | has no attribute | 'z' |
| --------------- | -------------- | ---------------- | --- |
Ifyouarenotsurewhattypeanobjectis,youcanask:
>>> type(p)
<class '__main__.Point'>
Youcanalsouseisinstancetocheckwhetheranobjectisaninstanceofaclass:
| >>> isinstance(p, | Point) |     |     |
| ----------------- | ------ | --- | --- |
True
If you are not sure whether an object has a particular attribute, you can use the built-in
functionhasattr:
| >>> hasattr(p, | 'x') |     |     |
| -------------- | ---- | --- | --- |
True
| >>> hasattr(p, | 'z') |     |     |
| -------------- | ---- | --- | --- |
False
Thefirstargumentcanbeanyobject;thesecondargumentisastringthatcontainsthename
oftheattribute.
Youcanalsouseatrystatementtoseeiftheobjecthastheattributesyouneed:
try:
x = p.x
except AttributeError:
x = 0
This approach can make it easier to write functions that work with different types; more
onthattopiciscomingupinSection17.9.
15.8 Glossary
class: Aprogrammer-definedtype. Aclassdefinitioncreatesanewclassobject.
classobject: An object that contains information about a programmer-defined type. The
classobjectcanbeusedtocreateinstancesofthetype.
| instance: Anobjectthatbelongstoaclass.                |                                                   |     |     |
| ----------------------------------------------------- | ------------------------------------------------- | --- | --- |
| instantiate: Tocreateanewobject.                      |                                                   |     |     |
| attribute: Oneofthenamedvaluesassociatedwithanobject. |                                                   |     |     |
| embeddedobject:                                       | Anobjectthatisstoredasanattributeofanotherobject. |     |     |
shallowcopy: To copy the contents of an object, including any references to embedded
objects;implementedbythecopyfunctioninthecopymodule.
deepcopy: To copy the contents of an object as well as any embedded objects, and any
objectsembeddedinthem,andsoon;implementedbythedeepcopyfunctioninthe
copymodule.
objectdiagram: A diagram that shows objects, their attributes, and the values of the at-
tributes.

154 Chapter15. Classesandobjects
15.9 Exercises
Exercise15.1. WriteadefinitionforaclassnamedCirclewithattributescenterandradius,
wherecenterisaPointobjectandradiusisanumber.
InstantiateaCircleobjectthatrepresentsacirclewithitscenterat(150,100)andradius75.
Writeafunctionnamedpoint_in_circlethattakesaCircleandaPointandreturnsTrueifthe
Pointliesinorontheboundaryofthecircle.
Writeafunctionnamedrect_in_circlethattakesaCircleandaRectangleandreturnsTrueif
theRectangleliesentirelyinorontheboundaryofthecircle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns
TrueifanyofthecornersoftheRectanglefallinsidetheCircle. Orasamorechallengingversion,
returnTrueifanypartoftheRectanglefallsinsidetheCircle.
Solution: https://thinkpython.com/code/Circle.py.
Exercise15.2. Writeafunctioncalleddraw_rectthattakesaTurtleobjectandaRectangleand
usestheTurtletodrawtheRectangle. SeeChapter4forexamplesusingTurtleobjects.
Writeafunctioncalleddraw_circlethattakesaTurtleandaCircleanddrawstheCircle.
Solution: https://thinkpython.com/code/draw.py.

| Chapter | 16  |           |     |
| ------- | --- | --------- | --- |
| Classes | and | functions |     |
Now that we know how to create new types, the next step is to write functions that take
programmer-defined objects as parameters and return them as results. In this chapter I
alsopresent“functionalprogrammingstyle”andtwonewprogramdevelopmentplans.
https://thinkpython.com/code/
| Code examples | from this chapter | are available | from |
| ------------- | ----------------- | ------------- | ---- |
Time1.py. Solutionstotheexercisesareathttps://thinkpython.com/code/Time1_soln.
py.
16.1 Time
Time
As another example of a programmer-defined type, we’ll define a class called that
| recordsthetimeofday. | Theclassdefinitionlookslikethis: |     |     |
| -------------------- | -------------------------------- | --- | --- |
class Time:
| """Represents | the time      | of day. |     |
| ------------- | ------------- | ------- | --- |
| attributes:   | hour, minute, | second  |     |
"""
WecancreateanewTimeobjectandassignattributesforhours,minutes,andseconds:
time = Time()
| time.hour = | 11   |     |     |
| ----------- | ---- | --- | --- |
| time.minute | = 59 |     |     |
| time.second | = 30 |     |     |
ThestatediagramfortheTimeobjectlookslikeFigure16.1.
Asanexercise,writeafunctioncalledprint_timethattakesaTimeobjectandprintsitin
theformhour:minute:second. theformatsequence'%.2d'printsanintegerusing
Hint:
atleasttwodigits,includingaleadingzeroifnecessary.
Write a boolean function called is_after that takes two Time objects, t1 and t2, and re-
turnsTrueift1followst2chronologicallyandFalseotherwise.
Challenge: don’tusean
ifstatement.

| 156 |     |     | Chapter16. | Classesandfunctions |
| --- | --- | --- | ---------- | ------------------- |
Time
|     |     | time hour | 11  |     |
| --- | --- | --------- | --- | --- |
minute 59
second 30
Figure16.1: Objectdiagram.
| 16.2 | Pure functions |     |     |     |
| ---- | -------------- | --- | --- | --- |
Inthenextfewsections,we’llwritetwofunctionsthataddtimevalues. Theydemonstrate
two kinds of functions: pure functions and modifiers. They also demonstrate a develop-
mentplanI’llcallprototypeandpatch,whichisawayoftacklingacomplexproblemby
startingwithasimpleprototypeandincrementallydealingwiththecomplications.
Hereisasimpleprototypeofadd_time:
| def add_time(t1, | t2):        |             |     |     |
| ---------------- | ----------- | ----------- | --- | --- |
| sum              | = Time()    |             |     |     |
| sum.hour         | = t1.hour   | + t2.hour   |     |     |
| sum.minute       | = t1.minute | + t2.minute |     |     |
| sum.second       | = t1.second | + t2.second |     |     |
| return           | sum         |             |     |     |
ThefunctioncreatesanewTimeobject,initializesitsattributes,andreturnsareferenceto
thenewobject. Thisiscalledapurefunctionbecauseitdoesnotmodifyanyoftheobjects
passedtoitasargumentsandithasnoeffect,likedisplayingavalueorgettinguserinput,
otherthanreturningavalue.
startcontainsthestarttimeofamovie,
Totestthisfunction,I’llcreatetwoTimeobjects:
like Monty Python and the Holy Grail, and duration contains the run time of the movie,
whichisonehour35minutes.
add_timefiguresoutwhenthemoviewillbedone.
| >>> start           | = Time()          |           |     |     |
| ------------------- | ----------------- | --------- | --- | --- |
| >>> start.hour      | = 9               |           |     |     |
| >>> start.minute    | = 45              |           |     |     |
| >>> start.second    | = 0               |           |     |     |
| >>> duration        | = Time()          |           |     |     |
| >>> duration.hour   | = 1               |           |     |     |
| >>> duration.minute | =                 | 35        |     |     |
| >>> duration.second | =                 | 0         |     |     |
| >>> done            | = add_time(start, | duration) |     |     |
>>> print_time(done)
10:80:00
10:80:00
The result, might not be what you were hoping for. The problem is that this
function does not deal with cases where the number of seconds or minutes adds up to
morethansixty. Whenthathappens,wehaveto“carry”theextrasecondsintotheminute
columnortheextraminutesintothehourcolumn.
Here’sanimprovedversion:

16.3. Modifiers 157
| def add_time(t1, | t2): |     |
| ---------------- | ---- | --- |
sum = Time()
| sum.hour      | = t1.hour   | + t2.hour   |
| ------------- | ----------- | ----------- |
| sum.minute    | = t1.minute | + t2.minute |
| sum.second    | = t1.second | + t2.second |
| if sum.second | >= 60:      |             |
| sum.second    | -=          | 60          |
| sum.minute    | +=          | 1           |
| if sum.minute | >= 60:      |             |
| sum.minute    | -=          | 60          |
| sum.hour      | += 1        |             |
return sum
Althoughthisfunctioniscorrect,itisstartingtogetbig. Wewillseeashorteralternative
later.
16.3 Modifiers
Sometimesitisusefulforafunctiontomodifytheobjectsitgetsasparameters.Inthatcase,
thechangesarevisibletothecaller. Functionsthatworkthiswayarecalledmodifiers.
increment,whichaddsagivennumberofsecondstoaTimeobject,canbewrittennaturally
| asamodifier.        | Hereisaroughdraft: |     |
| ------------------- | ------------------ | --- |
| def increment(time, | seconds):          |     |
| time.second         | += seconds         |     |
| if time.second      | >=                 | 60: |
| time.second         | -=                 | 60  |
| time.minute         | +=                 | 1   |
| if time.minute      | >=                 | 60: |
| time.minute         | -=                 | 60  |
| time.hour           | += 1               |     |
Thefirstlineperformsthebasicoperation; theremainderdealswiththespecialcaseswe
sawbefore.
Isthisfunctioncorrect? Whathappensifsecondsismuchgreaterthansixty?
Inthatcase,itisnotenoughtocarryonce; wehavetokeepdoingituntiltime.secondis
if while
less than sixty. One solution is to replace the statements with statements. That
would make the function correct, but not very efficient. As an exercise, write a correct
versionofincrementthatdoesn’tcontainanyloops.
Anything that can be done with modifiers can also be done with pure functions. In fact,
some programming languages only allow pure functions. There is some evidence that
programsthatusepurefunctionsarefastertodevelopandlesserror-pronethanprograms
thatusemodifiers. Butmodifiersareconvenientattimes,andfunctionalprogramstendto
belessefficient.

| 158 |     |     | Chapter16. | Classesandfunctions |
| --- | --- | --- | ---------- | ------------------- |
Ingeneral,Irecommendthatyouwritepurefunctionswheneveritisreasonableandresort
to modifiers only if there is a compelling advantage. This approach might be called a
functionalprogrammingstyle.
As an exercise, write a “pure” version of increment that creates and returns a new Time
objectratherthanmodifyingtheparameter.
| 16.4 Prototyping |     | versus planning |     |     |
| ---------------- | --- | --------------- | --- | --- |
ThedevelopmentplanIamdemonstratingiscalled“prototypeandpatch”. Foreachfunc-
tion,Iwroteaprototypethatperformedthebasiccalculationandthentestedit,patching
errorsalongtheway.
This approach can be effective, especially if you don’t yet have a deep understanding
of the problem. But incremental corrections can generate code that is unnecessarily
complicated—since it deals with many special cases—and unreliable—since it is hard to
knowifyouhavefoundalltheerrors.
Analternativeisdesigneddevelopment,inwhichhigh-levelinsightintotheproblemcan
maketheprogrammingmucheasier. Inthiscase,theinsightisthataTimeobjectisreally
athree-digitnumberinbase60(seehttp://en.wikipedia.org/wiki/Sexagesimal). The
secondattributeisthe“onescolumn”,theminuteattributeisthe“sixtiescolumn”,andthe
hourattributeisthe“thirty-sixhundredscolumn”.
Whenwewroteadd_timeandincrement,
wewereeffectivelydoingadditioninbase60,
whichiswhywehadtocarryfromonecolumntothenext.
Thisobservationsuggestsanotherapproachtothewholeproblem—wecanconvertTime
objects to integers and take advantage of the fact that the computer knows how to do
integerarithmetic.
HereisafunctionthatconvertsTimestointegers:
def time_to_int(time):
| minutes | = time.hour | * 60 + time.minute |     |     |
| ------- | ----------- | ------------------ | --- | --- |
| seconds | = minutes   | * 60 + time.second |     |     |
| return  | seconds     |                    |     |     |
AndhereisafunctionthatconvertsanintegertoaTime(recallthatdivmoddividesthefirst
argumentbythesecondandreturnsthequotientandremainderasatuple).
def int_to_time(seconds):
| time =     | Time()      |                   |     |     |
| ---------- | ----------- | ----------------- | --- | --- |
| minutes,   | time.second | = divmod(seconds, | 60) |     |
| time.hour, | time.minute | = divmod(minutes, | 60) |     |
| return     | time        |                   |     |     |
Youmighthavetothinkabit,andrunsometests,toconvinceyourselfthatthesefunctions
Onewaytotestthemistocheckthattime_to_int(int_to_time(x)) == xfor
arecorrect.
| manyvaluesofx. | Thisisanexampleofaconsistencycheck. |     |     |     |
| -------------- | ----------------------------------- | --- | --- | --- |
Onceyouareconvincedtheyarecorrect,youcanusethemtorewriteadd_time:
| def add_time(t1, | t2):                 |                   |     |     |
| ---------------- | -------------------- | ----------------- | --- | --- |
| seconds          | = time_to_int(t1)    | + time_to_int(t2) |     |     |
| return           | int_to_time(seconds) |                   |     |     |

16.5. Debugging 159
This version is shorter than the original, and easier to verify. As an exercise, rewrite
incrementusingtime_to_intandint_to_time.
Insomeways,convertingfrombase60tobase10andbackisharderthanjustdealingwith
times.Baseconversionismoreabstract;ourintuitionfordealingwithtimevaluesisbetter.
But if we have the insight to treat times as base 60 numbers and make the investment of
writingtheconversionfunctions(time_to_intandint_to_time),wegetaprogramthat
isshorter,easiertoreadanddebug,andmorereliable.
Itisalsoeasiertoaddfeatureslater. Forexample, imaginesubtractingtwoTimestofind
thedurationbetweenthem. Thenaiveapproachwouldbetoimplementsubtractionwith
borrowing. Usingtheconversionfunctionswouldbeeasierandmorelikelytobecorrect.
Ironically,sometimesmakingaproblemharder(ormoregeneral)makesiteasier(because
therearefewerspecialcasesandfeweropportunitiesforerror).
16.5 Debugging
A Time object is well-formed if the values of minute and second are between 0 and 60
(including0butnot60)andifhourispositive. hourandminuteshouldbeintegervalues,
butwemightallowsecondtohaveafractionpart.
Requirementslikethesearecalledinvariantsbecausetheyshouldalwaysbetrue. Toput
itadifferentway,iftheyarenottrue,somethinghasgonewrong.
Writingcodetocheckinvariantscanhelpdetecterrorsandfindtheircauses. Forexample,
youmighthaveafunctionlikevalid_timethattakesaTimeobjectandreturnsFalseifit
violatesaninvariant:
def valid_time(time):
| if time.hour   | < 0 or time.minute |             | < 0 or | time.second | < 0: |
| -------------- | ------------------ | ----------- | ------ | ----------- | ---- |
| return         | False              |             |        |             |      |
| if time.minute | >= 60 or           | time.second | >=     | 60:         |      |
| return         | False              |             |        |             |      |
return True
At the beginning of each function you could check the arguments to make sure they are
valid:
| def add_time(t1, | t2):                |                   |                 |               |     |
| ---------------- | ------------------- | ----------------- | --------------- | ------------- | --- |
| if not           | valid_time(t1) or   | not               | valid_time(t2): |               |     |
| raise            | ValueError('invalid |                   | Time object     | in add_time') |     |
| seconds          | = time_to_int(t1)   | + time_to_int(t2) |                 |               |     |
return int_to_time(seconds)
Oryoucoulduseanassertstatement,whichchecksagiveninvariantandraisesanexcep-
tionifitfails:
| def add_time(t1, | t2):               |                   |     |     |     |
| ---------------- | ------------------ | ----------------- | --- | --- | --- |
| assert           | valid_time(t1) and | valid_time(t2)    |     |     |     |
| seconds          | = time_to_int(t1)  | + time_to_int(t2) |     |     |     |
return int_to_time(seconds)
assertstatementsareusefulbecausetheydistinguishcodethatdealswithnormalcondi-
tionsfromcodethatchecksforerrors.

160 Chapter16. Classesandfunctions
16.6 Glossary
prototypeandpatch: A development plan that involves writing a rough draft of a pro-
gram,testing,andcorrectingerrorsastheyarefound.
designeddevelopment: A development plan that involves high-level insight into the
problem and more planning than incremental development or prototype develop-
ment.
purefunction: Afunctionthatdoesnotmodifyanyoftheobjectsitreceivesasarguments.
Mostpurefunctionsarefruitful.
modifier: Afunctionthatchangesoneormoreoftheobjectsitreceivesasarguments.Most
modifiersarevoid;thatis,theyreturnNone.
functionalprogrammingstyle: Astyleofprogramdesigninwhichthemajorityoffunc-
tionsarepure.
invariant: Aconditionthatshouldalwaysbetrueduringtheexecutionofaprogram.
assertstatement: Astatementthatchecksaconditionandraisesanexceptionifitfails.
16.7 Exercises
Code examples from this chapter are available from https://thinkpython.com/code/
Time1.py; solutionstotheexercisesareavailablefromhttps://thinkpython.com/code/
Time1_soln.py.
Exercise16.1. Writeafunctioncalledmul_timethattakesaTimeobjectandanumberandreturns
anewTimeobjectthatcontainstheproductoftheoriginalTimeandthenumber.
Thenusemul_timetowriteafunctionthattakesaTimeobjectthatrepresentsthefinishingtime
inarace,andanumberthatrepresentsthedistance,andreturnsaTimeobjectthatrepresentsthe
averagepace(timepermile).
Exercise 16.2. The datetime module provides time objects that are similar to the Time objects
in this chapter, but they provide a rich set of methods and operators. Read the documentation at
http://docs.python.org/3/library/datetime.html.
1. Usethedatetimemoduletowriteaprogramthatgetsthecurrentdateandprintsthedayof
theweek.
2. Writeaprogramthattakesabirthdayasinputandprintstheuser’sageandthenumberof
days,hours,minutesandsecondsuntiltheirnextbirthday.
3. For two people born on different days, there is a day when one is twice as old as the other.
That’s their Double Day. Write a program that takes two birth dates and computes their
DoubleDay.
4. For a little more challenge, write the more general version that computes the day when one
personisntimesolderthantheother.
Solution: https://thinkpython.com/code/double.py

Chapter 17
Classes and methods
Although we are using some of Python’s object-oriented features, the programs from the
last two chapters are not really object-oriented because they don’t represent the relation-
shipsbetweenprogrammer-definedtypesandthefunctionsthatoperateonthem.Thenext
stepistotransformthosefunctionsintomethodsthatmaketherelationshipsexplicit.
Code examples from this chapter are available from https://thinkpython.com/code/
Time2.py,andsolutionstotheexercisesareinhttps://thinkpython.com/code/Point2_
soln.py.
17.1 Object-oriented features
Python is an object-oriented programming language, which means that it provides fea-
turesthatsupportobject-orientedprogramming,whichhasthesedefiningcharacteristics:
• Programsincludeclassandmethoddefinitions.
• Mostofthecomputationisexpressedintermsofoperationsonobjects.
• Objectsoftenrepresentthingsintherealworld,andmethodsoftencorrespondtothe
waysthingsintherealworldinteract.
For example, the Time class defined in Chapter 16 corresponds to the way people record
thetimeofday,andthefunctionswedefinedcorrespondtothekindsofthingspeopledo
with times. Similarly, the Point and Rectangle classes in Chapter 15 correspond to the
mathematicalconceptsofapointandarectangle.
So far, we have not taken advantage of the features Python provides to support object-
oriented programming. These features are not strictly necessary; most of them provide
alternative syntax for things we have already done. But in many cases, the alternative is
moreconciseandmoreaccuratelyconveysthestructureoftheprogram.
Forexample,inTime1.pythereisnoobviousconnectionbetweentheclassdefinitionand
thefunctiondefinitionsthatfollow. Withsomeexamination,itisapparentthateveryfunc-
tiontakesatleastoneTimeobjectasanargument.

| 162 |     |     |     | Chapter17. | Classesandmethods |
| --- | --- | --- | --- | ---------- | ----------------- |
This observation is the motivation for methods; a method is a function that is associated
withaparticularclass. Wehaveseenmethodsforstrings,lists,dictionariesandtuples. In
thischapter,wewilldefinemethodsforprogrammer-definedtypes.
Methodsaresemanticallythesameasfunctions,buttherearetwosyntacticdifferences:
• Methods are defined inside a class definition in order to make the relationship be-
tweentheclassandthemethodexplicit.
• Thesyntaxforinvokingamethodisdifferentfromthesyntaxforcallingafunction.
In the next few sections, we will take the functions from the previous two chapters and
transformthemintomethods. Thistransformationispurelymechanical;youcandoitby
followingasequenceofsteps. Ifyouarecomfortableconvertingfromoneformtoanother,
youwillbeabletochoosethebestformforwhateveryouaredoing.
| 17.2 | Printing | objects |     |     |     |
| ---- | -------- | ------- | --- | --- | --- |
In Chapter 16, we defined a class named Time and in Section 16.1, you wrote a function
namedprint_time:
class Time:
| """Represents |     | the time | of day.""" |     |     |
| ------------- | --- | -------- | ---------- | --- | --- |
def print_time(time):
| print('%.2d:%.2d:%.2d' |     |     | % (time.hour, | time.minute, | time.second)) |
| ---------------------- | --- | --- | ------------- | ------------ | ------------- |
Tocallthisfunction,youhavetopassaTimeobjectasanargument:
| >>> start        | = Time() |      |     |     |     |
| ---------------- | -------- | ---- | --- | --- | --- |
| >>> start.hour   |          | = 9  |     |     |     |
| >>> start.minute |          | = 45 |     |     |     |
| >>> start.second |          | = 00 |     |     |     |
>>> print_time(start)
09:45:00
Tomakeprint_timeamethod,allwehavetodoismovethefunctiondefinitioninsidethe
| classdefinition. | Noticethechangeinindentation. |     |     |     |     |
| ---------------- | ----------------------------- | --- | --- | --- | --- |
class Time:
| def | print_time(time):      |     |               |              |               |
| --- | ---------------------- | --- | ------------- | ------------ | ------------- |
|     | print('%.2d:%.2d:%.2d' |     | % (time.hour, | time.minute, | time.second)) |
print_time.
Now there are two ways to call The first (and less common) way is to use
functionsyntax:
>>> Time.print_time(start)
09:45:00
Inthisuseofdotnotation,Timeisthenameoftheclass,andprint_timeisthenameofthe
method. startispassedasaparameter.
Thesecond(andmoreconcise)wayistousemethodsyntax:
>>> start.print_time()
09:45:00

17.3. Anotherexample 163
In this use of dot notation, print_time is the name of the method (again), and start is
the object the method is invoked on, which is called the subject. Just as the subject of
a sentence is what the sentence is about, the subject of a method invocation is what the
methodisabout.
Inside the method, the subject is assigned to the first parameter, so in this case start is
assignedtotime.
Byconvention,thefirstparameterofamethodiscalledself,soitwouldbemorecommon
towriteprint_timelikethis:
class Time:
def print_time(self):
print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
Thereasonforthisconventionisanimplicitmetaphor:
• Thesyntaxforafunctioncall, print_time(start), suggeststhatthefunctionisthe
active agent. It says something like, “Hey print_time! Here’s an object for you to
print.”
• Inobject-orientedprogramming,theobjectsaretheactiveagents. Amethodinvoca-
tionlikestart.print_time()says“Heystart! Pleaseprintyourself.”
Thischangeinperspectivemightbemorepolite,butitisnotobviousthatitisuseful.Inthe
exampleswehaveseensofar,itmaynotbe.Butsometimesshiftingresponsibilityfromthe
functionsontotheobjectsmakesitpossibletowritemoreversatilefunctions(ormethods),
andmakesiteasiertomaintainandreusecode.
Asanexercise,rewritetime_to_int(fromSection16.4)asamethod.Youmightbetempted
torewriteint_to_timeasamethod,too,butthatdoesn’treallymakesensebecausethere
wouldbenoobjecttoinvokeiton.
17.3 Another example
Here’saversionofincrement(fromSection16.3)rewrittenasamethod:
# inside class Time:
def increment(self, seconds):
seconds += self.time_to_int()
return int_to_time(seconds)
Thisversionassumesthattime_to_intiswrittenasamethod. Also,notethatitisapure
function,notamodifier.
Here’showyouwouldinvokeincrement:
>>> start.print_time()
09:45:00
>>> end = start.increment(1337)
>>> end.print_time()
10:07:17

| 164 |        |     |     | Chapter17. | Classesandmethods |       |
| --- | ------ | --- | --- | ---------- | ----------------- | ----- |
|     | start, |     |     | self.      |                   | 1337, |
The subject, gets assigned to the first parameter, The argument, gets
assignedtothesecondparameter,seconds.
This mechanism can be confusing, especially if you make an error. For example, if you
invokeincrementwithtwoarguments,youget:
| >>> end | = start.increment(1337, |     | 460) |     |     |     |
| ------- | ----------------------- | --- | ---- | --- | --- | --- |
TypeError: increment() takes 2 positional arguments but 3 were given
The error message is initially confusing, because there are only two arguments in paren-
theses. Butthesubjectisalsoconsideredanargument,soalltogetherthat’sthree.
By the way, a positional argument is an argument that doesn’t have a parameter name;
| thatis,itisnotakeywordargument. |       |            | Inthisfunctioncall: |     |     |     |
| ------------------------------- | ----- | ---------- | ------------------- | --- | --- | --- |
| sketch(parrot,                  | cage, | dead=True) |                     |     |     |     |
parrotandcagearepositional,anddeadisakeywordargument.
| 17.4 | A more complicated |     | example |     |     |     |
| ---- | ------------------ | --- | ------- | --- | --- | --- |
Rewritingis_after(fromSection16.1)isslightlymorecomplicatedbecauseittakestwo
Timeobjectsasparameters. Inthiscaseitisconventionaltonamethefirstparameterself
andthesecondparameterother:
| # inside | class Time:               |         |                       |     |     |     |
| -------- | ------------------------- | ------- | --------------------- | --- | --- | --- |
| def      | is_after(self,            | other): |                       |     |     |     |
|          | return self.time_to_int() |         | > other.time_to_int() |     |     |     |
Tousethismethod,youhavetoinvokeitononeobjectandpasstheotherasanargument:
>>> end.is_after(start)
True
OnenicethingaboutthissyntaxisthatitalmostreadslikeEnglish: “endisafterstart?”
| 17.5 | The init method |     |     |     |     |     |
| ---- | --------------- | --- | --- | --- | --- | --- |
Theinitmethod(shortfor“initialization”)isaspecialmethodthatgetsinvokedwhenan
__init__
object is instantiated. Its full name is (two underscore characters, followed by
init,andthentwomoreunderscores). AninitmethodfortheTimeclassmightlooklike
this:
| # inside | class Time:    |          |                      |     |     |     |
| -------- | -------------- | -------- | -------------------- | --- | --- | --- |
| def      | __init__(self, | hour=0,  | minute=0, second=0): |     |     |     |
|          | self.hour =    | hour     |                      |     |     |     |
|          | self.minute    | = minute |                      |     |     |     |
|          | self.second    | = second |                      |     |     |     |
Itiscommonfortheparametersof__init__tohavethesamenamesastheattributes. The
statement
|     | self.hour = | hour |     |     |     |     |
| --- | ----------- | ---- | --- | --- | --- | --- |

17.6. The__str__method 165
storesthevalueoftheparameterhourasanattributeofself.
The parameters are optional, so if you call Time with no arguments, you get the default
values.
>>> time = Time()
>>> time.print_time()
00:00:00
Ifyouprovideoneargument,itoverrideshour:
>>> time = Time (9)
>>> time.print_time()
09:00:00
Ifyouprovidetwoarguments,theyoverridehourandminute.
>>> time = Time(9, 45)
>>> time.print_time()
09:45:00
Andifyouprovidethreearguments,theyoverrideallthreedefaultvalues.
As an exercise, write an init method for the Point class that takes x and y as optional
parametersandassignsthemtothecorrespondingattributes.
17.6 The __str__ method
__str__isaspecialmethod,like__init__,thatissupposedtoreturnastringrepresenta-
tionofanobject.
Forexample,hereisastrmethodforTimeobjects:
# inside class Time:
def __str__(self):
return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
Whenyouprintanobject,Pythoninvokesthestrmethod:
>>> time = Time(9, 45)
>>> print(time)
09:45:00
WhenIwriteanewclass,Ialmostalwaysstartbywriting__init__,whichmakesiteasier
toinstantiateobjects,and__str__,whichisusefulfordebugging.
Asanexercise,writeastrmethodforthePointclass. CreateaPointobjectandprintit.
17.7 Operator overloading
By defining other special methods, you can specify the behavior of operators on
programmer-defined types. For example, if you define a method named __add__ for the
Timeclass,youcanusethe+operatoronTimeobjects.
Hereiswhatthedefinitionmightlooklike:

| 166      |               |                    |                       | Chapter17. | Classesandmethods |
| -------- | ------------- | ------------------ | --------------------- | ---------- | ----------------- |
| # inside | class Time:   |                    |                       |            |                   |
| def      | __add__(self, | other):            |                       |            |                   |
|          | seconds =     | self.time_to_int() | + other.time_to_int() |            |                   |
return int_to_time(seconds)
Andhereishowyoucoulduseit:
| >>> start       | = Time(9, | 45)       |     |     |     |
| --------------- | --------- | --------- | --- | --- | --- |
| >>> duration    | = Time(1, | 35)       |     |     |     |
| >>> print(start | +         | duration) |     |     |     |
11:20:00
Whenyouapplythe+operatortoTimeobjects,Pythoninvokes__add__. Whenyouprint
theresult,Pythoninvokes__str__.
Sothereisalothappeningbehindthescenes!
Changingthebehaviorofanoperatorsothatitworkswithprogrammer-definedtypesis
called operator overloading. For every operator in Python there is a corresponding spe-
cialmethod,like__add__. Formoredetails,seehttp://docs.python.org/3/reference/
datamodel.html#specialnames.
Asanexercise,writeanaddmethodforthePointclass.
| 17.8 | Type-based | dispatch |     |     |     |
| ---- | ---------- | -------- | --- | --- | --- |
In the previous section we added two Time objects, but you also might want to add an
__add__
integer to a Time object. The following is a version of that checks the type of
otherandinvokeseitheradd_timeorincrement:
| # inside | class Time:   |         |     |     |     |
| -------- | ------------- | ------- | --- | --- | --- |
| def      | __add__(self, | other): |     |     |     |
if isinstance(other, Time):
|     | return | self.add_time(other) |     |     |     |
| --- | ------ | -------------------- | --- | --- | --- |
else:
|     | return         | self.increment(other) |                       |     |     |
| --- | -------------- | --------------------- | --------------------- | --- | --- |
| def | add_time(self, | other):               |                       |     |     |
|     | seconds =      | self.time_to_int()    | + other.time_to_int() |     |     |
return int_to_time(seconds)
| def | increment(self, | seconds):          |     |     |     |
| --- | --------------- | ------------------ | --- | --- | --- |
|     | seconds +=      | self.time_to_int() |     |     |     |
return int_to_time(seconds)
Thebuilt-infunctionisinstancetakesavalueandaclassobject, andreturns Trueifthe
valueisaninstanceoftheclass.
IfotherisaTimeobject,__add__invokesadd_time.
Otherwiseitassumesthattheparam-
eter is a number and invokes increment. This operation is called a type-based dispatch
becauseitdispatchesthecomputationtodifferentmethodsbasedonthetypeoftheargu-
ments.
Hereareexamplesthatusethe+operatorwithdifferenttypes:

17.9. Polymorphism 167
| >>> start       | = Time(9, | 45)       |
| --------------- | --------- | --------- |
| >>> duration    | = Time(1, | 35)       |
| >>> print(start | +         | duration) |
11:20:00
| >>> print(start | +   | 1337) |
| --------------- | --- | ----- |
10:07:17
Unfortunately, this implementation of addition is not commutative. If the integer is the
firstoperand,youget
| >>> print(1337 | +   | start) |
| -------------- | --- | ------ |
TypeError: unsupported operand type(s) for +: 'int' and 'instance'
The problem is, instead of asking the Time object to add an integer, Python is asking an
integertoaddaTimeobject,anditdoesn’tknowhow. Butthereisacleversolutionforthis
problem: the special method __radd__, which stands for “right-side add”. This method
+
is invoked when a Time object appears on the right side of the operator. Here’s the
definition:
| # inside | class Time:    |         |
| -------- | -------------- | ------- |
| def      | __radd__(self, | other): |
return self.__add__(other)
Andhere’showit’sused:
| >>> print(1337 | +   | start) |
| -------------- | --- | ------ |
10:07:17
add
As an exercise, write an method for Points that works with either a Point object or a
tuple:
• If the second operand is a Point, the method should return a new Point whose x
coordinate is the sum of the x coordinates of the operands, and likewise for the y
coordinates.
• Ifthesecondoperandisatuple,themethodshouldaddthefirstelementofthetuple
to the x coordinate and the second element to the y coordinate, and return a new
Pointwiththeresult.
17.9 Polymorphism
Type-baseddispatchisusefulwhenitisnecessary,but(fortunately)itisnotalwaysneces-
sary. Often you can avoid it by writing functions that work correctly for arguments with
differenttypes.
Manyofthefunctionswewroteforstringsalsoworkforothersequencetypes. Forexam-
ple,inSection11.2weusedhistogramtocountthenumberoftimeseachletterappearsin
aword.
def histogram(s):
| d = | dict()   |       |
| --- | -------- | ----- |
| for | c in s:  |       |
|     | if c not | in d: |
|     | d[c]     | = 1   |

| 168 |     |     |     | Chapter17. | Classesandmethods |
| --- | --- | --- | --- | ---------- | ----------------- |
else:
|        | d[c] | = d[c]+1 |     |     |     |
| ------ | ---- | -------- | --- | --- | --- |
| return | d    |          |     |     |     |
Thisfunctionalsoworksforlists,tuples,andevendictionaries,aslongastheelementsof
sarehashable,sotheycanbeusedaskeysind.
| >>> t | = ['spam', | 'egg', 'spam', | 'spam', 'bacon', | 'spam'] |     |
| ----- | ---------- | -------------- | ---------------- | ------- | --- |
>>> histogram(t)
| {'bacon': | 1, 'egg': | 1, 'spam': | 4}  |     |     |
| --------- | --------- | ---------- | --- | --- | --- |
Functions that work with several types are called polymorphic. Polymorphism can fa-
sum,
cilitate code reuse. For example, the built-in function which adds the elements of a
sequence,worksaslongastheelementsofthesequencesupportaddition.
SinceTimeobjectsprovideanaddmethod,theyworkwithsum:
| >>> t1    | = Time(7,  | 43)      |     |     |     |
| --------- | ---------- | -------- | --- | --- | --- |
| >>> t2    | = Time(7,  | 41)      |     |     |     |
| >>> t3    | = Time(7,  | 37)      |     |     |     |
| >>> total | = sum([t1, | t2, t3]) |     |     |     |
>>> print(total)
23:01:00
In general, if all of the operations inside a function work with a given type, the function
workswiththattype.
Thebestkindofpolymorphismistheunintentionalkind,whereyoudiscoverthatafunc-
tionyoualreadywrotecanbeappliedtoatypeyouneverplannedfor.
| 17.10 | Debugging |     |     |     |     |
| ----- | --------- | --- | --- | --- | --- |
It is legal to add attributes to objects at any point in the execution of a program, but if
youhaveobjectswiththesametypethatdon’thavethesameattributes,itiseasytomake
mistakes. It is considered a good idea to initialize all of an object’s attributes in the init
method.
If you are not sure whether an object has a particular attribute, you can use the built-in
functionhasattr(seeSection15.7).
vars,
Another way to access attributes is the built-in function which takes an object and
returnsadictionarythatmapsfromattributenames(asstrings)totheirvalues:
| >>> p | = Point(3, | 4)  |     |     |     |
| ----- | ---------- | --- | --- | --- | --- |
>>> vars(p)
| {'y': | 4, 'x': | 3}  |     |     |     |
| ----- | ------- | --- | --- | --- | --- |
Forpurposesofdebugging,youmightfinditusefultokeepthisfunctionhandy:
def print_attributes(obj):
| for | attr in     | vars(obj):   |        |     |     |
| --- | ----------- | ------------ | ------ | --- | --- |
|     | print(attr, | getattr(obj, | attr)) |     |     |
print_attributes traverses the dictionary and prints each attribute name and its corre-
spondingvalue.
Thebuilt-infunctiongetattrtakesanobjectandanattributename(asastring)andreturns
theattribute’svalue.

17.11. Interfaceandimplementation 169
17.11 Interface and implementation
One of the goals of object-oriented design is to make software more maintainable, which
meansthatyoucankeeptheprogramworkingwhenotherpartsofthesystemchange,and
modifytheprogramtomeetnewrequirements.
A design principle that helps achieve that goal is to keep interfaces separate from imple-
mentations. Forobjects,thatmeansthatthemethodsaclassprovidesshouldnotdepend
onhowtheattributesarerepresented.
Forexample,inthischapterwedevelopedaclassthatrepresentsatimeofday. Methods
providedbythisclassincludetime_to_int,is_after,andadd_time.
We could implement those methods in several ways. The details of the implementation
dependonhowwerepresenttime. Inthischapter,theattributesofaTimeobjectarehour,
minute,andsecond.
Asanalternative,wecouldreplacetheseattributeswithasingleintegerrepresentingthe
numberofsecondssincemidnight. Thisimplementationwouldmakesomemethods,like
is_after,easiertowrite,butitmakesothermethodsharder.
Afteryoudeployanewclass,youmightdiscoverabetterimplementation. Ifotherparts
oftheprogramareusingyourclass,itmightbetime-consuminganderror-pronetochange
theinterface.
But if you designed the interface carefully, you can change the implementation without
changingtheinterface,whichmeansthatotherpartsoftheprogramdon’thavetochange.
17.12 Glossary
object-orientedlanguage: A language that provides features, such as programmer-
definedtypesandmethods,thatfacilitateobject-orientedprogramming.
object-orientedprogramming: Astyleofprogramminginwhichdataandtheoperations
thatmanipulateitareorganizedintoclassesandmethods.
method: Afunctionthatisdefinedinsideaclassdefinitionandisinvokedoninstancesof
thatclass.
subject: Theobjectamethodisinvokedon.
positionalargument: Anargumentthatdoesnotincludeaparametername,soitisnota
keywordargument.
operatoroverloading: Changing the behavior of an operator like + so it works with a
programmer-definedtype.
type-baseddispatch: Aprogrammingpatternthatchecksthetypeofanoperandandin-
vokesdifferentfunctionsfordifferenttypes.
polymorphic: Pertainingtoafunctionthatcanworkwithmorethanonetype.

170 Chapter17. Classesandmethods
17.13 Exercises
Exercise17.1. Downloadthecodefromthischapterfromhttps://thinkpython.com/code/
Time2.py. Change the attributes of Time to be a single integer representing seconds since mid-
night. Thenmodifythemethods(andthefunctionint_to_time)toworkwiththenewimplemen-
tation. Youshouldnothavetomodifythetestcodeinmain. Whenyouaredone,theoutputshould
bethesameasbefore. Solution: https://thinkpython.com/code/Time2_soln.py.
Exercise 17.2. This exercise is a cautionary tale about one of the most common, and difficult to
find,errorsinPython. WriteadefinitionforaclassnamedKangaroowiththefollowingmethods:
1. An__init__methodthatinitializesanattributenamedpouch_contentstoanemptylist.
2. A method named put_in_pouch that takes an object of any type and adds it to
pouch_contents.
3. A__str__methodthatreturnsastringrepresentationoftheKangarooobjectandthecon-
tentsofthepouch.
Test your code by creating two Kangaroo objects, assigning them to variables named kanga and
roo,andthenaddingrootothecontentsofkanga’spouch.
Downloadhttps://thinkpython.com/code/BadKangaroo.py. Itcontainsasolutiontothe
previousproblemwithonebig,nastybug. Findandfixthebug.
If you get stuck, you can download https://thinkpython.com/code/GoodKangaroo.py,
whichexplainstheproblemanddemonstratesasolution.

Chapter 18
Inheritance
The language feature most often associated with object-oriented programming is inheri-
tance. Inheritance is the ability to define a new class that is a modified version of an ex-
istingclass. InthischapterIdemonstrateinheritanceusingclassesthatrepresentplaying
cards,decksofcards,andpokerhands.
Ifyoudon’tplaypoker,youcanreadaboutitathttp://en.wikipedia.org/wiki/Poker,
butyoudon’thaveto;I’lltellyouwhatyouneedtoknowfortheexercises.
Code examples from this chapter are available from https://thinkpython.com/code/
Card.py.
18.1 Card objects
Therearefifty-twocardsinadeck, eachofwhichbelongstooneoffoursuitsandoneof
thirteenranks. ThesuitsareSpades,Hearts,Diamonds,andClubs(indescendingorderin
bridge). TheranksareAce, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, andKing. Dependingon
thegamethatyouareplaying,anAcemaybehigherthanKingorlowerthan2.
If we want to define a new object to represent a playing card, it is obvious what the at-
tributesshouldbe: rankandsuit. Itisnotasobviouswhattypetheattributesshouldbe.
One possibility is to use strings containing words like 'Spade' for suits and 'Queen' for
ranks.Oneproblemwiththisimplementationisthatitwouldnotbeeasytocomparecards
toseewhichhadahigherrankorsuit.
An alternative is to use integers to encode the ranks and suits. In this context, “encode”
means that we are going to define a mapping between numbers and suits, or between
numbers and ranks. This kind of encoding is not meant to be a secret (that would be
“encryption”).
Forexample,thistableshowsthesuitsandthecorrespondingintegercodes:
Spades (cid:55)→ 3
Hearts (cid:55)→ 2
Diamonds (cid:55)→ 1
Clubs (cid:55)→ 0

| 172 |     |     |     |     | Chapter18. | Inheritance |
| --- | --- | --- | --- | --- | ---------- | ----------- |
Thiscodemakesiteasytocomparecards;becausehighersuitsmaptohighernumbers,we
cancomparesuitsbycomparingtheircodes.
The mapping for ranks is fairly obvious; each of the numerical ranks maps to the corre-
spondinginteger,andforfacecards:
| Jack (cid:55)→  | 11  |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
| Queen (cid:55)→ | 12  |     |     |     |     |     |
| King (cid:55)→  | 13  |     |     |     |     |     |
Iamusingthe (cid:55)→ symboltomakeitclearthatthesemappingsarenotpartofthePython
program.Theyarepartoftheprogramdesign,buttheydon’tappearexplicitlyinthecode.
TheclassdefinitionforCardlookslikethis:
class Card:
| """Represents      | a standard |         | playing  | card.""" |     |     |
| ------------------ | ---------- | ------- | -------- | -------- | --- | --- |
| def __init__(self, |            | suit=0, | rank=2): |          |     |     |
self.suit = suit
self.rank = rank
Asusual,theinitmethodtakesanoptionalparameterforeachattribute. Thedefaultcard
isthe2ofClubs.
TocreateaCard,youcallCardwiththesuitandrankofthecardyouwant.
| queen_of_diamonds | = Card(1,  |     | 12) |     |     |     |
| ----------------- | ---------- | --- | --- | --- | --- | --- |
| 18.2 Class        | attributes |     |     |     |     |     |
In order to print Card objects in a way that people can easily read, we need a mapping
from the integer codes to the corresponding ranks and suits. A natural way to do that is
| withlistsofstrings. | Weassigntheseliststoclassattributes: |             |                              |           |                |     |
| ------------------- | ------------------------------------ | ----------- | ---------------------------- | --------- | -------------- | --- |
| # inside class      | Card:                                |             |                              |           |                |     |
| suit_names          | = ['Clubs',                          | 'Diamonds', |                              | 'Hearts', | 'Spades']      |     |
| rank_names          | = [None,                             | 'Ace',      | '2',                         | '3', '4', | '5', '6', '7', |     |
|                     | '8', '9',                            | '10',       | 'Jack',                      | 'Queen',  | 'King']        |     |
| def __str__(self):  |                                      |             |                              |           |                |     |
| return              | '%s of                               | %s' %       | (Card.rank_names[self.rank], |           |                |     |
Card.suit_names[self.suit])
Variables like suit_names and rank_names, which are defined inside a class but outside
ofanymethod,arecalledclassattributesbecausetheyareassociatedwiththeclassobject
Card.
Thistermdistinguishesthemfromvariableslikesuitandrank,whicharecalledinstance
attributesbecausetheyareassociatedwithaparticularinstance.
Both kinds of attribute are accessed using dot notation. For example, in __str__, self
|     |     | self.rank |     |     | Card |     |
| --- | --- | --------- | --- | --- | ---- | --- |
is a Card object, and is its rank. Similarly, is a class object, and
Card.rank_namesisalistofstringsassociatedwiththeclass.

18.3. Comparingcards 173
type list
Card suit_names
list
rank_names
Card
card1 suit 1
rank 11
Figure18.1: Objectdiagram.
Every card has its own suit and rank, but there is only one copy of suit_names and
rank_names.
Putting it all together, the expression Card.rank_names[self.rank] means “use the at-
tributerankfromtheobjectselfasanindexintothelistrank_namesfromtheclassCard,
andselecttheappropriatestring.”
Thefirstelementofrank_namesisNonebecausethereisnocardwithrankzero. Byinclud-
ingNoneasaplace-keeper,wegetamappingwiththenicepropertythattheindex2maps
tothestring'2',andsoon. Toavoidthistweak,wecouldhaveusedadictionaryinstead
ofalist.
Withthemethodswehavesofar,wecancreateandprintcards:
>>> card1 = Card(2, 11)
>>> print(card1)
Jack of Hearts
Figure 18.1 is a diagram of the Card class object and one Card instance. Card is a class
object; its type is type. card1 is an instance of Card, so its type is Card. To save space, I
didn’tdrawthecontentsofsuit_namesandrank_names.
18.3 Comparing cards
Forbuilt-intypes,therearerelationaloperators(<,>,==,etc.) thatcomparevaluesandde-
terminewhenoneisgreaterthan,lessthan,orequaltoanother. Forprogrammer-defined
types,wecanoverridethebehaviorofthebuilt-inoperatorsbyprovidingamethodnamed
__lt__,whichstandsfor“lessthan”.
__lt__takestwoparameters,selfandother,andreturnsTrueifselfisstrictlylessthan
other.
Thecorrectorderingforcardsisnotobvious. Forexample,whichisbetter,the3ofClubs
orthe2ofDiamonds? Onehasahigherrank,buttheotherhasahighersuit. Inorderto
comparecards,youhavetodecidewhetherrankorsuitismoreimportant.
Theanswermightdependonwhatgameyouareplaying,buttokeepthingssimple,we’ll
makethearbitrarychoicethatsuitismoreimportant,soalloftheSpadesoutrankallofthe
Diamonds,andsoon.

| 174 |     |     | Chapter18. | Inheritance |
| --- | --- | --- | ---------- | ----------- |
Withthatdecided,wecanwrite__lt__:
| # inside class Card: |         |     |     |     |
| -------------------- | ------- | --- | --- | --- |
| def __lt__(self,     | other): |     |     |     |
# check the suits
| if self.suit | < other.suit: | return True  |     |     |
| ------------ | ------------- | ------------ | --- | --- |
| if self.suit | > other.suit: | return False |     |     |
| # suits are  | the same...   | check ranks  |     |     |
return self.rank < other.rank
Youcanwritethismoreconciselyusingtuplecomparison:
| # inside class Card: |         |     |     |     |
| -------------------- | ------- | --- | --- | --- |
| def __lt__(self,     | other): |     |     |     |
t1 = self.suit, self.rank
t2 = other.suit, other.rank
return t1 < t2
As an exercise, write an __lt__ method for Time objects. You can use tuple comparison,
butyoualsomightconsidercomparingintegers.
18.4 Decks
NowthatwehaveCards,thenextstepistodefineDecks.Sinceadeckismadeupofcards,
itisnaturalforeachDecktocontainalistofcardsasanattribute.
ThefollowingisaclassdefinitionforDeck. Theinitmethodcreatestheattributecardsand
generatesthestandardsetoffifty-twocards:
class Deck:
def __init__(self):
self.cards = []
for suit in range(4):
| for rank | in range(1,  | 14):  |     |     |
| -------- | ------------ | ----- | --- | --- |
| card     | = Card(suit, | rank) |     |     |
self.cards.append(card)
Theeasiestwaytopopulatethedeckiswithanestedloop. Theouterloopenumeratesthe
suitsfrom0to3. Theinnerloopenumeratestheranksfrom1to13. Eachiterationcreates
anewCardwiththecurrentsuitandrank,andappendsittoself.cards.
| 18.5 Printing | the deck |     |     |     |
| ------------- | -------- | --- | --- | --- |
Hereisa__str__methodforDeck:
| # inside class Deck: |     |     |     |     |
| -------------------- | --- | --- | --- | --- |
def __str__(self):
res = []

18.6. Add,remove,shuffleandsort 175
for card in self.cards:
res.append(str(card))
return '\n'.join(res)
This method demonstrates an efficient way to accumulate a large string: building a list
of strings and then using the string method join. The built-in function str invokes the
__str__methodoneachcardandreturnsthestringrepresentation.
Sinceweinvokejoinonanewlinecharacter,thecardsareseparatedbynewlines. Here’s
whattheresultlookslike:
| >>> deck = | Deck() |     |     |
| ---------- | ------ | --- | --- |
>>> print(deck)
Ace of Clubs
2 of Clubs
3 of Clubs
...
10 of Spades
| Jack of Spades  |     |     |     |
| --------------- | --- | --- | --- |
| Queen of Spades |     |     |     |
| King of Spades  |     |     |     |
Eventhoughtheresultappearson52lines,itisonelongstringthatcontainsnewlines.
| 18.6 Add, | remove, | shuffle and | sort |
| --------- | ------- | ----------- | ---- |
To deal cards, we would like a method that removes a card from the deck and returns it.
Thelistmethodpopprovidesaconvenientwaytodothat:
| # inside class      | Deck: |     |     |
| ------------------- | ----- | --- | --- |
| def pop_card(self): |       |     |     |
return self.cards.pop()
Sincepopremovesthelastcardinthelist,wearedealingfromthebottomofthedeck.
Toaddacard,wecanusethelistmethodappend:
| # inside class     | Deck: |        |     |
| ------------------ | ----- | ------ | --- |
| def add_card(self, |       | card): |     |
self.cards.append(card)
Amethodlikethisthatusesanothermethodwithoutdoingmuchworkissometimescalled
aveneer. Themetaphorcomesfromwoodworking,whereaveneerisathinlayerofgood
qualitywoodgluedtothesurfaceofacheaperpieceofwoodtoimprovetheappearance.
Inthiscaseadd_cardisa“thin”methodthatexpressesalistoperationintermsappropriate
| fordecks. Itimprovestheappearance,orinterface,oftheimplementation. |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- |
As another example, we can write a Deck method named shuffle using the function
shufflefromtherandommodule:
| # inside class     | Deck: |     |     |
| ------------------ | ----- | --- | --- |
| def shuffle(self): |       |     |     |
random.shuffle(self.cards)

| 176 |     |     | Chapter18. | Inheritance |
| --- | --- | --- | ---------- | ----------- |
Don’tforgettoimportrandom.
Asanexercise,writeaDeckmethodnamedsortthatusesthelistmethodsorttosortthe
cardsinaDeck. sortusesthe__lt__methodwedefinedtodeterminetheorder.
18.7 Inheritance
Inheritanceistheabilitytodefineanewclassthatisamodifiedversionofanexistingclass.
As an example, let’s say we want a class to represent a “hand”, that is, the cards held by
oneplayer. Ahandissimilartoadeck: botharemadeupofacollectionofcards,andboth
requireoperationslikeaddingandremovingcards.
A hand is also different from a deck; there are operations we want for hands that don’t
makesenseforadeck. Forexample,inpokerwemightcomparetwohandstoseewhich
onewins. Inbridge,wemightcomputeascoreforahandinordertomakeabid.
This relationship between classes—similar, but different—lends itself to inheritance. To
define a new class that inherits from an existing class, you put the name of the existing
classinparentheses:
class Hand(Deck):
| """Represents |     | a hand of playing cards.""" |     |     |
| ------------- | --- | --------------------------- | --- | --- |
ThisdefinitionindicatesthatHandinheritsfromDeck;thatmeanswecanusemethodslike
pop_cardandadd_cardforHandsaswellasDecks.
When a new class inherits from an existing one, the existing one is called the parent and
thenewclassiscalledthechild.
Inthisexample,Handinherits__init__fromDeck,butitdoesn’treallydowhatwewant:
insteadofpopulatingthehandwith52newcards, theinitmethodforHandsshouldini-
tializecardswithanemptylist.
IfweprovideaninitmethodintheHandclass,itoverridestheoneintheDeckclass:
| # inside | class Hand:    |            |     |     |
| -------- | -------------- | ---------- | --- | --- |
| def      | __init__(self, | label=''): |     |     |
|          | self.cards     | = []       |     |     |
|          | self.label     | = label    |     |     |
WhenyoucreateaHand,Pythoninvokesthisinitmethod,nottheoneinDeck.
| >>> hand | = Hand('new | hand') |     |     |
| -------- | ----------- | ------ | --- | --- |
>>> hand.cards
[]
>>> hand.label
'new hand'
TheothermethodsareinheritedfromDeck,sowecanusepop_cardandadd_cardtodeal
acard:
| >>> deck | = Deck()          |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| >>> card | = deck.pop_card() |     |     |     |
>>> hand.add_card(card)
>>> print(hand)
| King of | Spades |     |     |     |
| ------- | ------ | --- | --- | --- |

18.8. Classdiagrams 177
Anaturalnextstepistoencapsulatethiscodeinamethodcalledmove_cards:
# inside class Deck:
def move_cards(self, hand, num):
for i in range(num):
hand.add_card(self.pop_card())
move_cardstakestwoarguments,aHandobjectandthenumberofcardstodeal. Itmodi-
fiesbothselfandhand,andreturnsNone.
In some games, cards are moved from one hand to another, or from a hand back to the
deck. Youcanusemove_cardsforanyoftheseoperations: selfcanbeeitheraDeckora
Hand,andhand,despitethename,canalsobeaDeck.
Inheritanceisausefulfeature.Someprogramsthatwouldberepetitivewithoutinheritance
canbewrittenmoreelegantlywithit. Inheritancecanfacilitatecodereuse, sinceyoucan
customize the behavior of parent classes without having to modify them. In some cases,
the inheritance structure reflects the natural structure of the problem, which makes the
designeasiertounderstand.
On the other hand, inheritance can make programs difficult to read. When a method is
invoked, it is sometimes not clear where to find its definition. The relevant code may be
spreadacrossseveralmodules.Also,manyofthethingsthatcanbedoneusinginheritance
canbedoneaswellorbetterwithoutit.
18.8 Class diagrams
So far we have seen stack diagrams, which show the state of a program, and object dia-
grams,whichshowtheattributesofanobjectandtheirvalues. Thesediagramsrepresent
asnapshotintheexecutionofaprogram,sotheychangeastheprogramruns.
Theyarealsohighlydetailed; forsomepurposes,toodetailed. Aclassdiagramisamore
abstract representation of the structure of a program. Instead of showing individual ob-
jects,itshowsclassesandtherelationshipsbetweenthem.
Thereareseveralkindsofrelationshipbetweenclasses:
• Objectsinoneclassmightcontainreferencestoobjectsinanotherclass. Forexample,
eachRectanglecontainsareferencetoaPoint,andeachDeckcontainsreferencesto
many Cards. This kind of relationship is called HAS-A, as in, “a Rectangle has a
Point.”
• Oneclassmightinheritfromanother. ThisrelationshipiscalledIS-A,asin,“aHand
isakindofaDeck.”
• One class might depend on another in the sense that objects in one class take ob-
jectsinthesecondclassasparameters,oruseobjectsinthesecondclassaspartofa
computation. Thiskindofrelationshipiscalledadependency.
A class diagram is a graphical representation of these relationships. For example, Fig-
ure18.2showstherelationshipsbetweenCard,DeckandHand.

178 Chapter18. Inheritance
*
Deck Card
Hand
Figure18.2: Classdiagram.
ThearrowwithahollowtriangleheadrepresentsanIS-Arelationship;inthiscaseitindi-
catesthatHandinheritsfromDeck.
The standard arrow head represents a HAS-A relationship; in this case a Deck has refer-
encestoCardobjects.
Thestar(*)nearthearrowheadisamultiplicity;itindicateshowmanyCardsaDeckhas.
Amultiplicitycanbeasimplenumber,like52,arange,like5..7orastar,whichindicates
thataDeckcanhaveanynumberofCards.
Therearenodependenciesinthisdiagram. Theywouldnormallybeshownwithadashed
arrow. Oriftherearealotofdependencies,theyaresometimesomitted.
A more detailed diagram might show that a Deck actually contains a list of Cards, but
built-intypeslikelistanddictareusuallynotincludedinclassdiagrams.
18.9 Debugging
Inheritancecanmakedebuggingdifficultbecausewhenyouinvokeamethodonanobject,
itmightbehardtofigureoutwhichmethodwillbeinvoked.
Suppose you are writing a function that works with Hand objects. You would like it to
workwithallkindsofHands,likePokerHands,BridgeHands,etc. Ifyouinvokeamethod
likeshuffle,youmightgettheonedefinedinDeck,butifanyofthesubclassesoverride
this method, you’ll get that version instead. This behavior is usually a good thing, but it
canbeconfusing.
Any time you are unsure about the flow of execution through your program, the sim-
plest solution is to add print statements at the beginning of the relevant methods. If
Deck.shuffleprintsamessagethatsayssomethinglike Running Deck.shuffle, thenas
theprogramrunsittracestheflowofexecution.
Asanalternative, youcouldusethisfunction, whichtakesanobjectandamethodname
(asastring)andreturnstheclassthatprovidesthedefinitionofthemethod:
def find_defining_class(obj, meth_name):
for ty in type(obj).mro():
if meth_name in ty.__dict__:
return ty
Here’sanexample:
>>> hand = Hand()
>>> find_defining_class(hand, 'shuffle')
<class '__main__.Deck'>

18.10. Dataencapsulation 179
SotheshufflemethodforthisHandistheoneinDeck.
find_defining_classusesthemromethodtogetthelistofclassobjects(types)thatwillbe
searchedformethods.“MRO”standsfor“methodresolutionorder”,whichisthesequence
ofclassesPythonsearchesto“resolve”amethodname.
Here’sadesignsuggestion: whenyouoverrideamethod,theinterfaceofthenewmethod
shouldbethesameastheold. Itshouldtakethesameparameters, returnthesametype,
andobeythesamepreconditionsandpostconditions. Ifyoufollowthisrule,youwillfind
thatanyfunctiondesignedtoworkwithaninstanceofaparentclass,likeaDeck,willalso
workwithinstancesofchildclasseslikeaHandandPokerHand.
Ifyouviolatethisrule,whichiscalledthe“Liskovsubstitutionprinciple”,yourcodewill
collapselike(sorry)ahouseofcards.
18.10 Data encapsulation
The previous chapters demonstrate a development plan we might call “object-oriented
design”. Weidentifiedobjectsweneeded—likePoint,RectangleandTime—anddefined
classes to represent them. In each case there is an obvious correspondence between the
objectandsomeentityintherealworld(oratleastamathematicalworld).
But sometimes it is less obvious what objects you need and how they should interact. In
that case you need a different development plan. In the same way that we discovered
function interfaces by encapsulation and generalization, we can discover class interfaces
bydataencapsulation.
Markov analysis, from Section 13.8, provides a good example. If you download my
codefromhttps://thinkpython.com/code/markov.py, you’llseethatitusestwoglobal
variables—suffix_mapandprefix—thatarereadandwrittenfromseveralfunctions.
suffix_map = {}
prefix = ()
Becausethesevariablesareglobal,wecanonlyrunoneanalysisatatime. Ifwereadtwo
texts,theirprefixesandsuffixeswouldbeaddedtothesamedatastructures(whichmakes
forsomeinterestinggeneratedtext).
To run multiple analyses, and keep them separate, we can encapsulate the state of each
analysisinanobject. Here’swhatthatlookslike:
class Markov:
def __init__(self):
self.suffix_map = {}
self.prefix = ()
Next,wetransformthefunctionsintomethods. Forexample,here’sprocess_word:
def process_word(self, word, order=2):
if len(self.prefix) < order:
self.prefix += (word,)
return

| 180 |     |     |     | Chapter18. | Inheritance |
| --- | --- | --- | --- | ---------- | ----------- |
try:
self.suffix_map[self.prefix].append(word)
except KeyError:
|             | # if                         | there is no entry    | for this prefix, | make one |     |
| ----------- | ---------------------------- | -------------------- | ---------------- | -------- | --- |
|             | self.suffix_map[self.prefix] |                      | = [word]         |          |     |
| self.prefix |                              | = shift(self.prefix, | word)            |          |     |
Transformingaprogramlikethis—changingthedesignwithoutchangingthebehavior—is
anotherexampleofrefactoring(seeSection4.7).
Thisexamplesuggestsadevelopmentplanfordesigningobjectsandmethods:
1. Startbywritingfunctionsthatreadandwriteglobalvariables(whennecessary).
2. Once you get the program working, look for associations between global variables
andthefunctionsthatusethem.
3. Encapsulaterelatedvariablesasattributesofanobject.
4. Transformtheassociatedfunctionsintomethodsofthenewclass.
https://thinkpython.com/code/
| As an exercise, | download | my Markov | code from |     |     |
| --------------- | -------- | --------- | --------- | --- | --- |
markov.py,
and follow the steps described above to encapsulate the global variables
as attributes of a new class called Markov. Solution: https://thinkpython.com/code/
markov2.py.
| 18.11 | Glossary |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
encode: Torepresentonesetofvaluesusinganothersetofvaluesbyconstructingamap-
pingbetweenthem.
classattribute: An attribute associated with a class object. Class attributes are defined
insideaclassdefinitionbutoutsideanymethod.
| instanceattribute: |     | Anattributeassociatedwithaninstanceofaclass. |     |     |     |
| ------------------ | --- | -------------------------------------------- | --- | --- | --- |
veneer: Amethodorfunctionthatprovidesadifferentinterfacetoanotherfunctionwith-
outdoingmuchcomputation.
inheritance: The ability to define a new class that is a modified version of a previously
definedclass.
| parentclass: | Theclassfromwhichachildclassinherits. |     |     |     |     |
| ------------ | ------------------------------------- | --- | --- | --- | --- |
childclass: A new class created by inheriting from an existing class; also called a “sub-
class”.
| IS-Arelationship: |     | Arelationshipbetweenachildclassanditsparentclass. |     |     |     |
| ----------------- | --- | ------------------------------------------------- | --- | --- | --- |
HAS-Arelationship: Arelationshipbetweentwoclasseswhereinstancesofoneclasscon-
tainreferencestoinstancesoftheother.
dependency: A relationship between two classes where instances of one class use in-
stancesoftheotherclass,butdonotstorethemasattributes.

18.12. Exercises 181
classdiagram: A diagram that shows the classes in a program and the relationships be-
tweenthem.
multiplicity: A notation in a class diagram that shows, for a HAS-A relationship, how
manyreferencestherearetoinstancesofanotherclass.
dataencapsulation: Aprogramdevelopmentplanthatinvolvesaprototypeusingglobal
variablesandafinalversionthatmakestheglobalvariablesintoinstanceattributes.
18.12 Exercises
Exercise18.1. Forthefollowingprogram,drawaUMLclassdiagramthatshowstheseclassesand
therelationshipsamongthem.
class PingPongParent:
pass
class Ping(PingPongParent):
def __init__(self, pong):
self.pong = pong
class Pong(PingPongParent):
def __init__(self, pings=None):
if pings is None:
self.pings = []
else:
self.pings = pings
def add_ping(self, ping):
self.pings.append(ping)
pong = Pong()
ping = Ping(pong)
pong.add_ping(ping)
Exercise18.2. WriteaDeckmethodcalleddeal_handsthattakestwoparameters,thenumberof
handsandthenumberofcardsperhand. ItshouldcreatetheappropriatenumberofHandobjects,
dealtheappropriatenumberofcardsperhand,andreturnalistofHands.
Exercise 18.3. The following are the possible hands in poker, in increasing order of value and
decreasingorderofprobability:
pair: twocardswiththesamerank
twopair: twopairsofcardswiththesamerank
threeofakind: threecardswiththesamerank
straight: fivecardswithranksinsequence(acescanbehighorlow,soAce-2-3-4-5isastraight
andsois10-Jack-Queen-King-Ace,butQueen-King-Ace-2-3isnot.)
flush: fivecardswiththesamesuit
fullhouse: threecardswithonerank,twocardswithanother

182 Chapter18. Inheritance
fourofakind: fourcardswiththesamerank
straightflush: fivecardsinsequence(asdefinedabove)andwiththesamesuit
Thegoaloftheseexercisesistoestimatetheprobabilityofdrawingthesevarioushands.
1. Downloadthefollowingfilesfromhttps://thinkpython.com/code:
Card.py : AcompleteversionoftheCard,DeckandHandclassesinthischapter.
PokerHand.py : Anincompleteimplementationofaclassthatrepresentsapokerhand,and
somecodethattestsit.
2. IfyourunPokerHand.py,itdealsseven7-cardpokerhandsandcheckstoseeifanyofthem
containsaflush. Readthiscodecarefullybeforeyougoon.
3. Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True or
False according to whether or not the hand meets the relevant criteria. Your code should
workcorrectlyfor“hands”thatcontainanynumberofcards(although5and7arethemost
commonsizes).
4. Writeamethodnamedclassifythatfiguresoutthehighest-valueclassificationforahand
andsetsthelabelattributeaccordingly. Forexample,a7-cardhandmightcontainaflush
andapair;itshouldbelabeled“flush”.
5. Whenyouareconvincedthatyourclassificationmethodsareworking,thenextstepistoesti-
matetheprobabilitiesofthevarioushands. WriteafunctioninPokerHand.pythatshuffles
a deck of cards, divides it into hands, classifies the hands, and counts the number of times
variousclassificationsappear.
6. Printatableoftheclassificationsandtheirprobabilities. Runyourprogramwithlargerand
larger numbers of hands until the output values converge to a reasonable degree of accu-
racy. Compare your results to the values at http://en.wikipedia.org/wiki/Hand_
rankings.
Solution: https://thinkpython.com/code/PokerHandSoln.py.

Chapter 19
The Goodies
One of my goals for this book has been to teach you as little Python as possible. When
thereweretwowaystodosomething,Ipickedoneandavoidedmentioningtheother. Or
sometimesIputthesecondoneintoanexercise.
Now I want to go back for some of the good bits that got left behind. Python provides a
numberoffeaturesthatarenotreallynecessary—youcanwritegoodcodewithoutthem—
butwiththemyoucansometimeswritecodethat’smoreconcise,readableorefficient,and
sometimesallthree.
19.1 Conditional expressions
We saw conditional statements in Section 5.4. Conditional statements are often used to
chooseoneoftwovalues;forexample:
if x > 0:
y = math.log(x)
else:
y = float('nan')
Thisstatementcheckswhetherxispositive. Ifso,itcomputesmath.log. Ifnot,math.log
wouldraiseaValueError. Toavoidstoppingtheprogram,wegeneratea“NaN”,whichis
aspecialfloating-pointvaluethatrepresents“NotaNumber”.
Wecanwritethisstatementmoreconciselyusingaconditionalexpression:
y = math.log(x) if x > 0 else float('nan')
YoucanalmostreadthislinelikeEnglish: “ygetslog-xifxisgreaterthan0; otherwiseit
getsNaN”.
Recursivefunctionscansometimesberewrittenusingconditionalexpressions. Forexam-
ple,hereisarecursiveversionoffactorial:
def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n-1)

| 184 |     |     | Chapter19. | TheGoodies |
| --- | --- | --- | ---------- | ---------- |
Wecanrewriteitlikethis:
def factorial(n):
| return 1 | if n == 0 else | n * factorial(n-1) |     |     |
| -------- | -------------- | ------------------ | --- | --- |
Anotheruseofconditionalexpressionsishandlingoptionalarguments. Forexample,here
istheinitmethodfromGoodKangaroo(seeExercise17.2):
| def __init__(self, | name, | contents=None): |     |     |
| ------------------ | ----- | --------------- | --- | --- |
self.name = name
if contents == None:
contents = []
self.pouch_contents = contents
Wecanrewritethisonelikethis:
| def __init__(self, | name, | contents=None): |     |     |
| ------------------ | ----- | --------------- | --- | --- |
self.name = name
| self.pouch_contents |     | = [] if contents | == None else | contents |
| ------------------- | --- | ---------------- | ------------ | -------- |
In general, you can replace a conditional statement with a conditional expression if both
branchescontainsimpleexpressionsthatareeitherreturnedorassignedtothesamevari-
able.
| 19.2 List | comprehensions |     |     |     |
| --------- | -------------- | --- | --- | --- |
InSection10.7wesawthemapandfilterpatterns. Forexample, thisfunctiontakesalist
of strings, maps the string method capitalize to the elements, and returns a new list of
strings:
def capitalize_all(t):
| res = [] |     |     |     |     |
| -------- | --- | --- | --- | --- |
| for s in | t:  |     |     |     |
res.append(s.capitalize())
| return res |     |     |     |     |
| ---------- | --- | --- | --- | --- |
Wecanwritethismoreconciselyusingalistcomprehension:
def capitalize_all(t):
| return [s.capitalize() |     | for s in t] |     |     |
| ---------------------- | --- | ----------- | --- | --- |
The bracket operators indicate that we are constructing a new list. The expression inside
thebracketsspecifiestheelementsofthelist, andtheforclauseindicateswhatsequence
wearetraversing.
Thesyntaxofalistcomprehensionisalittleawkwardbecausetheloopvariable,sinthis
example,appearsintheexpressionbeforewegettothedefinition.
Listcomprehensionscanalsobeusedforfiltering. Forexample,thisfunctionselectsonly
theelementsoftthatareuppercase,andreturnsanewlist:
def only_upper(t):
| res = [] |     |     |     |     |
| -------- | --- | --- | --- | --- |
| for s in | t:  |     |     |     |
if s.isupper():
res.append(s)
| return res |     |     |     |     |
| ---------- | --- | --- | --- | --- |

19.3. Generatorexpressions 185
Wecanrewriteitusingalistcomprehension
def only_upper(t):
return [s for s in t if s.isupper()]
Listcomprehensionsareconciseandeasytoread,atleastforsimpleexpressions.Andthey
areusuallyfasterthantheequivalentforloops,sometimesmuchfaster. Soifyouaremad
atmefornotmentioningthemearlier,Iunderstand.
But,inmydefense,listcomprehensionsarehardertodebugbecauseyoucan’tputaprint
statement inside the loop. I suggest that you use them only if the computation is simple
enoughthatyouarelikelytogetitrightthefirsttime. Andforbeginnersthatmeansnever.
19.3 Generator expressions
Generatorexpressionsaresimilartolistcomprehensions,butwithparenthesesinsteadof
squarebrackets:
>>> g = (x**2 for x in range(5))
>>> g
<generator object <genexpr> at 0x7f4c45a786c0>
Theresultisageneratorobjectthatknowshowtoiteratethroughasequenceofvalues.But
unlikealistcomprehension,itdoesnotcomputethevaluesallatonce;itwaitstobeasked.
Thebuilt-infunctionnextgetsthenextvaluefromthegenerator:
>>> next(g)
0
>>> next(g)
1
When you get to the end of the sequence, next raises a StopIteration exception. You can
alsouseaforlooptoiteratethroughthevalues:
>>> for val in g:
... print(val)
4
9
16
The generator object keeps track of where it is in the sequence, so the for loop picks up
wherenextleftoff. Oncethegeneratorisexhausted,itcontinuestoraiseStopIteration:
>>> next(g)
StopIteration
Generatorexpressionsareoftenusedwithfunctionslikesum,max,andmin:
>>> sum(x**2 for x in range(5))
30
19.4 any and all
Python provides a built-in function, any, that takes a sequence of boolean values and re-
turnsTrueifanyofthevaluesareTrue. Itworksonlists:

| 186             |        |        |     | Chapter19. | TheGoodies |
| --------------- | ------ | ------ | --- | ---------- | ---------- |
| >>> any([False, | False, | True]) |     |            |            |
True
Butitisoftenusedwithgeneratorexpressions:
| >>> any(letter | == 't' for | letter | in 'monty') |     |     |
| -------------- | ---------- | ------ | ----------- | --- | --- |
True
in
That example isn’t very useful because it does the same thing as the operator. But we
coulduseanytorewritesomeofthesearchfunctionswewroteinSection9.3. Forexample,
wecouldwriteavoidslikethis:
| def avoids(word, | forbidden): |              |            |          |     |
| ---------------- | ----------- | ------------ | ---------- | -------- | --- |
| return not       | any(letter  | in forbidden | for letter | in word) |     |
ThefunctionalmostreadslikeEnglish,“wordavoidsforbiddeniftherearenotanyforbid-
denlettersinword.”
Usinganywithageneratorexpressionisefficientbecauseitstopsimmediatelyifitfindsa
Truevalue,soitdoesn’thavetoevaluatethewholesequence.
|     |     |     | all, | True |     |
| --- | --- | --- | ---- | ---- | --- |
Python provides another built-in function, that returns if every element of the
sequenceisTrue. Asanexercise,usealltore-writeuses_allfromSection9.3.
19.5 Sets
InSection13.6Iusedictionariestofindthewordsthatappearinadocumentbutnotina
wordlist. ThefunctionIwrotetakesd1,whichcontainsthewordsfromthedocumentas
keys,andd2,whichcontainsthelistofwords.
Itreturnsadictionarythatcontainsthekeys
fromd1thatarenotind2.
| def subtract(d1, | d2):   |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- |
| res = dict()     |        |     |     |     |     |
| for key          | in d1: |     |     |     |     |
if key not in d2:
|            | res[key] = | None |     |     |     |
| ---------- | ---------- | ---- | --- | --- | --- |
| return res |            |      |     |     |     |
Inallofthesedictionaries,thevaluesareNonebecauseweneverusethem.
Asaresult,we
wastesomestoragespace.
set,
Python provides another built-in type, called a that behaves like a collection of dic-
tionarykeyswithnovalues. Addingelementstoasetisfast;soischeckingmembership.
Andsetsprovidemethodsandoperatorstocomputecommonsetoperations.
Forexample,setsubtractionisavailableasamethodcalleddifferenceorasanoperator,
-. Sowecanrewritesubtractlikethis:
| def subtract(d1, | d2):      |     |     |     |     |
| ---------------- | --------- | --- | --- | --- | --- |
| return set(d1)   | - set(d2) |     |     |     |     |
Theresultisasetinsteadofadictionary, butforoperationslikeiteration, thebehavioris
thesame.
Some of the exercises in this book can be done concisely and efficiently with sets. For
example,hereisasolutiontohas_duplicates,fromExercise10.7,thatusesadictionary:

19.6. Counters 187
def has_duplicates(t):
| d = {}   |     |     |     |
| -------- | --- | --- | --- |
| for x in | t:  |     |     |
if x in d:
return True
d[x] = True
| return | False |     |     |
| ------ | ----- | --- | --- |
Whenanelementappearsforthefirsttime,itisaddedtothedictionary.Ifthesameelement
appearsagain,thefunctionreturnsTrue.
Usingsets,wecanwritethesamefunctionlikethis:
def has_duplicates(t):
| return | len(set(t)) | < len(t) |     |
| ------ | ----------- | -------- | --- |
Anelementcanonlyappearinasetonce,soifanelementintappearsmorethanonce,the
setwillbesmallerthant. Iftherearenoduplicates,thesetwillbethesamesizeast.
WecanalsousesetstodosomeoftheexercisesinChapter9. Forexample,here’saversion
ofuses_onlywithaloop:
| def uses_only(word, | available): |               |     |
| ------------------- | ----------- | ------------- | --- |
| for letter          | in word:    |               |     |
| if                  | letter not  | in available: |     |
return False
| return | True |     |     |
| ------ | ---- | --- | --- |
uses_onlycheckswhetheralllettersinwordareinavailable.
Wecanrewriteitlikethis:
| def uses_only(word, | available):  |                |     |
| ------------------- | ------------ | -------------- | --- |
| return              | set(word) <= | set(available) |     |
The<=operatorcheckswhetheronesetisasubsetofanother,includingthepossibilitythat
theyareequal,whichistrueifallthelettersinwordappearinavailable.
Asanexercise,rewriteavoidsusingsets.
19.6 Counters
A Counter is like a set, except that if an element appears more than once, the Counter
keepstrackofhowmanytimesitappears. Ifyouarefamiliarwiththemathematicalidea
ofamultiset,aCounterisanaturalwaytorepresentamultiset.
Counterisdefinedinastandardmodulecalledcollections,soyouhavetoimportit.You
caninitializeaCounterwithastring,list,oranythingelsethatsupportsiteration:
| >>> from collections | import            | Counter |     |
| -------------------- | ----------------- | ------- | --- |
| >>> count =          | Counter('parrot') |         |     |
>>> count
| Counter({'r': | 2, 't': | 1, 'o': 1, 'p': | 1, 'a': 1}) |
| ------------- | ------- | --------------- | ----------- |
Countersbehavelikedictionariesinmanyways;theymapfromeachkeytothenumberof
| timesitappears. | Asindictionaries,thekeyshavetobehashable. |     |     |
| --------------- | ----------------------------------------- | --- | --- |
Unlikedictionaries,Countersdon’traiseanexceptionifyouaccessanelementthatdoesn’t
appear. Instead,theyreturn0:

| 188 |     |     | Chapter19. | TheGoodies |
| --- | --- | --- | ---------- | ---------- |
>>> count['d']
0
WecanuseCounterstorewriteis_anagramfromExercise10.6:
| def is_anagram(word1, | word2): |                |     |     |
| --------------------- | ------- | -------------- | --- | --- |
| return Counter(word1) | ==      | Counter(word2) |     |     |
If two words are anagrams, they contain the same letters with the same counts, so their
Countersareequivalent.
Counters provide methods and operators to perform set-like operations, including ad-
dition, subtraction, union and intersection. And they provide an often-useful method,
most_common, whichreturnsalistofvalue-frequencypairs, sortedfrommostcommonto
least:
| >>> count = Counter('parrot') |                               |     |     |     |
| ----------------------------- | ----------------------------- | --- | --- | --- |
| >>> for val,                  | freq in count.most_common(3): |     |     |     |
| ... print(val,                | freq)                         |     |     |     |
r 2
p 1
a 1
19.7 defaultdict
Thecollectionsmodulealsoprovidesdefaultdict,whichislikeadictionaryexceptthat
ifyouaccessakeythatdoesn’texist,itcangenerateanewvalueonthefly.
Whenyoucreateadefaultdict,youprovideafunctionthat’susedtocreatenewvalues. A
function used to create objects is sometimes called a factory. The built-in functions that
createlists,sets,andothertypescanbeusedasfactories:
| >>> from collections | import defaultdict |     |     |     |
| -------------------- | ------------------ | --- | --- | --- |
>>> d = defaultdict(list)
Notice that the argument is list, which is a class object, not list(), which is a new list.
Thefunctionyouprovidedoesn’tgetcalledunlessyouaccessakeythatdoesn’texist.
| >>> t = d['new | key'] |     |     |     |
| -------------- | ----- | --- | --- | --- |
>>> t
[]
Thenewlist,whichwe’recallingt,isalsoaddedtothedictionary. Soifwemodifyt,the
changeappearsind:
| >>> t.append('new | value') |     |     |     |
| ----------------- | ------- | --- | --- | --- |
>>> d
| defaultdict(<class | 'list'>, {'new | key': ['new | value']}) |     |
| ------------------ | -------------- | ----------- | --------- | --- |
Ifyouaremakingadictionaryoflists,youcanoftenwritesimplercodeusingdefaultdict.
InmysolutiontoExercise12.2,whichyoucangetfromhttps://thinkpython.com/code/
anagram_sets.py,Imakeadictionarythatmapsfromasortedstringofletterstothelistof
wordsthatcanbespelledwiththoseletters.Forexample,’opst’mapstothelist[’opts’,
| ’post’, ’pots’, | ’spot’, ’stop’, | ’tops’]. |     |     |
| --------------- | --------------- | -------- | --- | --- |
Here’stheoriginalcode:

19.8. Namedtuples 189
def all_anagrams(filename):
d = {}
| for line in open(filename): |     |     |
| --------------------------- | --- | --- |
word = line.strip().lower()
t = signature(word)
| if t not in | d:     |     |
| ----------- | ------ | --- |
| d[t] =      | [word] |     |
else:
d[t].append(word)
return d
Thiscanbesimplifiedusingsetdefault,whichyoumighthaveusedinExercise11.2:
def all_anagrams(filename):
d = {}
| for line in open(filename): |     |     |
| --------------------------- | --- | --- |
word = line.strip().lower()
t = signature(word)
| d.setdefault(t, | []).append(word) |     |
| --------------- | ---------------- | --- |
return d
Thissolutionhasthedrawbackthatitmakesanewlisteverytime,regardlessofwhether
itisneeded. Forlists,that’snobigdeal,butifthefactoryfunctioniscomplicated,itmight
be.
Wecanavoidthisproblemandsimplifythecodeusingadefaultdict:
def all_anagrams(filename):
d = defaultdict(list)
| for line in open(filename): |     |     |
| --------------------------- | --- | --- |
word = line.strip().lower()
t = signature(word)
d[t].append(word)
return d
whichyoucandownloadfromhttps://thinkpython.com/
MysolutiontoExercise18.3,
code/PokerHandSoln.py,usessetdefaultinthefunctionhas_straightflush. Thissolu-
tionhasthedrawbackofcreatingaHandobjecteverytimethroughtheloop,whetheritis
neededornot. Asanexercise,rewriteitusingadefaultdict.
| 19.8 Named | tuples |     |
| ---------- | ------ | --- |
Many simple objects are basically collections of related values. For example, the Point
objectdefinedinChapter15containstwonumbers,xandy.
Whenyoudefineaclasslike
this,youusuallystartwithaninitmethodandastrmethod:
class Point:
| def __init__(self, | x=0, y=0): |     |
| ------------------ | ---------- | --- |
| self.x = x         |            |     |
| self.y = y         |            |     |
def __str__(self):
| return '(%g, | %g)' % (self.x, | self.y) |
| ------------ | --------------- | ------- |

190 Chapter19. TheGoodies
This is a lot of code to convey a small amount of information. Python provides a more
concisewaytosaythesamething:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
Thefirstargumentisthenameoftheclassyouwanttocreate. Thesecondisalistofthe
attributesPointobjectsshouldhave,asstrings.Thereturnvaluefromnamedtupleisaclass
object:
>>> Point
<class '__main__.Point'>
Point automatically provides methods like __init__ and __str__ so you don’t have to
writethem.
TocreateaPointobject,youusethePointclassasafunction:
>>> p = Point(1, 2)
>>> p
Point(x=1, y=2)
The init method assigns the arguments to attributes using the names you provided. The
strmethodprintsarepresentationofthePointobjectanditsattributes.
Youcanaccesstheelementsofthenamedtuplebyname:
>>> p.x, p.y
(1, 2)
Butyoucanalsotreatanamedtupleasatuple:
>>> p[0], p[1]
(1, 2)
>>> x, y = p
>>> x, y
(1, 2)
Namedtuplesprovideaquickwaytodefinesimpleclasses. Thedrawbackisthatsimple
classes don’t always stay simple. You might decide later that you want to add methods
toanamedtuple. Inthatcase,youcoulddefineanewclassthatinheritsfromthenamed
tuple:
class Pointier(Point):
# add more methods here
Oryoucouldswitchtoaconventionalclassdefinition.
19.9 Gathering keyword args
InSection12.4,wesawhowtowriteafunctionthatgathersitsargumentsintoatuple:
def printall(*args):
print(args)
Youcancallthisfunctionwithanynumberofpositionalarguments(thatis,argumentsthat
don’thavekeywords):

19.10. Glossary 191
| >>> printall(1, |      | 2.0, '3') |     |     |     |     |
| --------------- | ---- | --------- | --- | --- | --- | --- |
| (1, 2.0,        | '3') |           |     |     |     |     |
Butthe*operatordoesn’tgatherkeywordarguments:
| >>> printall(1, |            | 2.0, third='3') |               |         |                  |     |
| --------------- | ---------- | --------------- | ------------- | ------- | ---------------- | --- |
| TypeError:      | printall() | got             | an unexpected | keyword | argument 'third' |     |
Togatherkeywordarguments,youcanusethe**operator:
| def printall(*args, |     | **kwargs): |     |     |     |     |
| ------------------- | --- | ---------- | --- | --- | --- | --- |
| print(args,         |     | kwargs)    |     |     |     |     |
Youcancallthekeywordgatheringparameteranythingyouwant,butkwargsisacommon
choice. Theresultisadictionarythatmapsfromkeywordstovalues:
| >>> printall(1, |           | 2.0, third='3') |     |     |     |     |
| --------------- | --------- | --------------- | --- | --- | --- | --- |
| (1, 2.0)        | {'third': | '3'}            |     |     |     |     |
**
If you have a dictionary of keywords and values, you can use the scatter operator, to
callafunction:
| >>> d = | dict(x=1, | y=2) |     |     |     |     |
| ------- | --------- | ---- | --- | --- | --- | --- |
>>> Point(**d)
| Point(x=1, | y=2) |     |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- | --- |
Withoutthescatteroperator,thefunctionwouldtreatdasasinglepositionalargument,so
itwouldassigndtoxandcomplainbecausethere’snothingtoassigntoy:
| >>> d = | dict(x=1, | y=2) |     |     |     |     |
| ------- | --------- | ---- | --- | --- | --- | --- |
>>> Point(d)
| Traceback  | (most      | recent call | last):      |            |           |     |
| ---------- | ---------- | ----------- | ----------- | ---------- | --------- | --- |
| File       | "<stdin>", | line 1,     | in <module> |            |           |     |
| TypeError: | __new__()  | missing     | 1 required  | positional | argument: | 'y' |
Whenyouareworkingwithfunctionsthathavealargenumberofparameters,itisoften
usefultocreateandpassarounddictionariesthatspecifyfrequentlyusedoptions.
| 19.10 | Glossary |     |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- | --- |
conditionalexpression: Anexpressionthathasoneoftwovalues,dependingonacondi-
tion.
for
listcomprehension: An expression with a loop in square brackets that yields a new
list.
generatorexpression: Anexpressionwithaforloopinparenthesesthatyieldsagenera-
torobject.
multiset: Amathematicalentitythatrepresentsamappingbetweentheelementsofaset
andthenumberoftimestheyappear.
factory: Afunction,usuallypassedasaparameter,usedtocreateobjects.

| 192             |     |     |     | Chapter19. | TheGoodies |
| --------------- | --- | --- | --- | ---------- | ---------- |
| 19.11 Exercises |     |     |     |            |            |
Exercise19.1. Thefollowingisafunctionthatcomputesthebinomialcoefficientrecursively.
| def binomial_coeff(n, | k):          |             |           |     |     |
| --------------------- | ------------ | ----------- | --------- | --- | --- |
| """Compute            | the binomial | coefficient | "n choose | k". |     |
| n: number             | of trials    |             |           |     |     |
| k: number             | of successes |             |           |     |     |
| returns:              | int          |             |           |     |     |
"""
| if k == | 0:  |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
return 1
| if n == | 0:  |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
return 0
| res = binomial_coeff(n-1, |     | k) + binomial_coeff(n-1, |     | k-1) |     |
| ------------------------- | --- | ------------------------ | --- | ---- | --- |
| return res                |     |                          |     |      |     |
Rewritethebodyofthefunctionusingnestedconditionalexpressions.
Onenote: thisfunctionisnotveryefficientbecauseitendsupcomputingthesamevaluesoverand
over. Youcouldmakeitmoreefficientbymemoizing(seeSection11.6). Butyouwillfindthatit’s
hardertomemoizeifyouwriteitusingconditionalexpressions.

Appendix A
Debugging
Whenyouaredebugging,youshoulddistinguishamongdifferentkindsoferrorsinorder
totrackthemdownmorequickly:
• Syntaxerrorsarediscoveredbytheinterpreterwhenitistranslatingthesourcecode
intobytecode. Theyindicatethatthereissomethingwrongwiththestructureofthe
program. Example: Omitting the colon at the end of a def statement generates the
somewhatredundantmessageSyntaxError: invalid syntax.
• Runtime errors are produced by the interpreter if something goes wrong while the
programisrunning. Mostruntimeerrormessagesincludeinformationaboutwhere
the error occurred and what functions were executing. Example: An infinite recur-
sion eventually causes the runtime error “maximum recursion depth exceeded”.
• Semanticerrorsareproblemswithaprogramthatrunswithoutproducingerrormes-
sagesbutdoesn’tdotherightthing. Example: Anexpressionmaynotbeevaluated
intheorderyouexpect,yieldinganincorrectresult.
Thefirststepindebuggingistofigureoutwhichkindoferroryouaredealingwith. Al-
thoughthefollowingsectionsareorganizedbyerrortype,sometechniquesareapplicable
inmorethanonesituation.
A.1 Syntax errors
Syntax errors are usually easy to fix once you figure out what they are. Unfortunately,
the error messages are often not helpful. The most common messages are SyntaxError:
invalid syntax and SyntaxError: invalid token, neither of which is very informa-
tive.
Ontheotherhand,themessagedoestellyouwhereintheprogramtheproblemoccurred.
Actually,ittellsyouwherePythonnoticedaproblem,whichisnotnecessarilywherethe
error is. Sometimes the error is prior to the location of the error message, often on the
precedingline.

194 AppendixA. Debugging
Ifyouarebuildingtheprogramincrementally,youshouldhaveagoodideaaboutwhere
theerroris. Itwillbeinthelastlineyouadded.
If you are copying code from a book, start by comparing your code to the book’s code
verycarefully. Checkeverycharacter. Atthesametime,rememberthatthebookmightbe
wrong,soifyouseesomethingthatlookslikeasyntaxerror,itmightbe.
Herearesomewaystoavoidthemostcommonsyntaxerrors:
1. MakesureyouarenotusingaPythonkeywordforavariablename.
2. Checkthatyouhaveacolonattheendoftheheaderofeverycompoundstatement,
includingfor,while,if,anddefstatements.
3. Make sure that any strings in the code have matching quotation marks. Make sure
thatallquotationmarksare“straightquotes”,not“curlyquotes”.
4. If you have multiline strings with triple quotes (single or double), make sure you
haveterminatedthestringproperly. Anunterminatedstringmaycauseaninvalid
token error at the end of your program, or it may treat the following part of the
programasastringuntilitcomestothenextstring. Inthesecondcase,itmightnot
produceanerrormessageatall!
5. Anunclosedopeningoperator—(,{,or[—makesPythoncontinuewiththenextline
aspartofthecurrentstatement. Generally,anerroroccursalmostimmediatelyinthe
nextline.
6. Checkfortheclassic=insteadof==insideaconditional.
7. Check the indentation to make sure it lines up the way it is supposed to. Python
canhandlespaceandtabs,butifyoumixthemitcancauseproblems. Thebestway
toavoidthisproblemistouseatexteditorthatknowsaboutPythonandgenerates
consistentindentation.
8. Ifyouhavenon-ASCIIcharactersinthecode(includingstringsandcomments),that
mightcauseaproblem,althoughPython3usuallyhandlesnon-ASCIIcharacters. Be
carefulifyoupasteintextfromawebpageorothersource.
Ifnothingworks,moveontothenextsection...
A.1.1 Ikeepmakingchangesanditmakesnodifference.
Iftheinterpretersaysthereisanerrorandyoudon’tseeit,thatmightbebecauseyouand
theinterpreterarenotlookingatthesamecode. Checkyourprogrammingenvironmentto
makesurethattheprogramyouareeditingistheonePythonistryingtorun.
Ifyouarenotsure,tryputtinganobviousanddeliberatesyntaxerroratthebeginningof
the program. Now run it again. If the interpreter doesn’t find the new error, you are not
runningthenewcode.
Thereareafewlikelyculprits:
• You edited the file and forgot to save the changes before running it again. Some
programmingenvironmentsdothisforyou,butsomedon’t.

A.2. Runtimeerrors 195
• Youchangedthenameofthefile,butyouarestillrunningtheoldname.
• Somethinginyourdevelopmentenvironmentisconfiguredincorrectly.
• Ifyouarewritingamoduleandusingimport,makesureyoudon’tgiveyourmodule
thesamenameasoneofthestandardPythonmodules.
• If you are using import to read a module, remember that you have to restart the
interpreterorusereloadtoreadamodifiedfile. Ifyouimportthemoduleagain,it
doesn’tdoanything.
Ifyougetstuckandyoucan’tfigureoutwhatisgoingon, oneapproachistostartagain
withanewprogramlike“Hello,World!”,andmakesureyoucangetaknownprogramto
run. Thengraduallyaddthepiecesoftheoriginalprogramtothenewone.
A.2 Runtime errors
Onceyourprogramissyntacticallycorrect,Pythoncanreaditandatleaststartrunningit.
Whatcouldpossiblygowrong?
A.2.1 Myprogramdoesabsolutelynothing.
This problem is most common when your file consists of functions and classes but does
notactuallyinvokeafunctiontostartexecution. Thismaybeintentionalifyouonlyplan
toimportthismoduletosupplyclassesandfunctions.
Ifitisnotintentional,makesurethereisafunctioncallintheprogram,andmakesurethe
flowofexecutionreachesit(see“FlowofExecution”below).
A.2.2 Myprogramhangs.
Ifaprogramstopsandseemstobedoingnothing,itis“hanging”. Oftenthatmeansthatit
iscaughtinaninfinitelooporinfiniterecursion.
• If there is a particular loop that you suspect is the problem, add a print statement
immediatelybeforetheloopthatsays“enteringtheloop”andanotherimmediately
afterthatsays“exitingtheloop”.
Run the program. If you get the first message and not the second, you’ve got an
infiniteloop. Gotothe“InfiniteLoop”sectionbelow.
• Mostofthetime,aninfiniterecursionwillcausetheprogramtorunforawhileand
then produce a “RuntimeError: Maximum recursion depth exceeded” error. If that
happens,gotothe“InfiniteRecursion”sectionbelow.
If you are not getting this error but you suspect there is a problem with a recursive
methodorfunction, youcanstillusethetechniquesinthe“InfiniteRecursion”sec-
tion.
• Ifneitherofthosestepsworks,starttestingotherloopsandotherrecursivefunctions
andmethods.
• Ifthatdoesn’twork,thenitispossiblethatyoudon’tunderstandtheflowofexecu-
tioninyourprogram. Gotothe“FlowofExecution”sectionbelow.

| 196 |     |     |     | AppendixA. | Debugging |
| --- | --- | --- | --- | ---------- | --------- |
InfiniteLoop
If you think you have an infinite loop and you think you know what loop is causing the
problem,addaprintstatementattheendoftheloopthatprintsthevaluesofthevariables
intheconditionandthevalueofthecondition.
Forexample:
| while x           | > 0 and y | < 0 :   |               |     |     |
| ----------------- | --------- | ------- | ------------- | --- | --- |
| # do              | something | to x    |               |     |     |
| # do              | something | to y    |               |     |     |
| print('x:         | ',        | x)      |               |     |     |
| print('y:         | ',        | y)      |               |     |     |
| print("condition: |           | ", (x > | 0 and y < 0)) |     |     |
Nowwhenyouruntheprogram,youwillseethreelinesofoutputforeachtimethrough
Thelasttimethroughtheloop,theconditionshouldbeFalse.
| theloop. |     |     |     | Iftheloopkeeps |     |
| -------- | --- | --- | --- | -------------- | --- |
going,youwillbeabletoseethevaluesofxandy,andyoumightfigureoutwhytheyare
notbeingupdatedcorrectly.
InfiniteRecursion
Mostofthetime,infiniterecursioncausestheprogramtorunforawhileandthenproduce
| aMaximum | recursion | depth exceedederror. |     |     |     |
| -------- | --------- | -------------------- | --- | --- | --- |
Ifyoususpectthatafunctioniscausinganinfiniterecursion,makesurethatthereisabase
case. Thereshouldbesomeconditionthatcausesthefunctiontoreturnwithoutmakinga
recursiveinvocation. Ifnot,youneedtorethinkthealgorithmandidentifyabasecase.
print
If there is a base case but the program doesn’t seem to be reaching it, add a state-
mentatthebeginningofthefunctionthatprintstheparameters. Nowwhenyourunthe
program, you will see a few lines of output every time the function is invoked, and you
willseetheparametervalues. Iftheparametersarenotmovingtowardthebasecase,you
willgetsomeideasaboutwhynot.
FlowofExecution
Ifyouarenotsurehowtheflowofexecutionismovingthroughyourprogram,addprint
statementstothebeginningofeachfunctionwithamessagelike“enteringfunctionfoo”,
wherefooisthenameofthefunction.
Nowwhenyouruntheprogram,itwillprintatraceofeachfunctionasitisinvoked.
A.2.3 WhenIruntheprogramIgetanexception.
Ifsomethinggoeswrongduringruntime,Pythonprintsamessagethatincludesthename
oftheexception,thelineoftheprogramwheretheproblemoccurred,andatraceback.
Thetracebackidentifiesthefunctionthatiscurrentlyrunning, andthenthefunctionthat
called it, and then the function that called that, and so on. In other words, it traces the

A.2. Runtimeerrors 197
sequenceoffunctioncallsthatgotyoutowhereyouare,includingthelinenumberinyour
filewhereeachcalloccurred.
The first step is to examine the place in the program where the error occurred and see if
youcanfigureoutwhathappened. Thesearesomeofthemostcommonruntimeerrors:
NameError: Youaretryingtouseavariablethatdoesn’texistinthecurrentenvironment.
Checkifthenameisspelledright,oratleastconsistently. Andrememberthatlocal
variablesarelocal;youcannotrefertothemfromoutsidethefunctionwheretheyare
defined.
TypeError: Thereareseveralpossiblecauses:
• You are trying to use a value improperly. Example: indexing a string, list, or
tuplewithsomethingotherthananinteger.
• Thereisamismatchbetweentheitemsinaformatstringandtheitemspassed
forconversion. Thiscanhappenifeitherthenumberofitemsdoesnotmatchor
aninvalidconversioniscalledfor.
• You are passing the wrong number of arguments to a function. For methods,
look at the method definition and check that the first parameter is self. Then
look at the method invocation; make sure you are invoking the method on an
objectwiththerighttypeandprovidingtheotherargumentscorrectly.
KeyError: Youaretryingtoaccessanelementofadictionaryusingakeythatthedictio-
narydoesnotcontain. Ifthekeysarestrings,rememberthatcapitalizationmatters.
AttributeError: Youaretryingtoaccessanattributeormethodthatdoesnotexist. Check
thespelling! Youcanusethebuilt-infunctionvarstolisttheattributesthatdoexist.
IfanAttributeErrorindicatesthatanobjecthasNoneType,thatmeansthatitisNone.
Sotheproblemisnottheattributename,buttheobject.
Thereasontheobjectisnonemightbethatyouforgottoreturnavaluefromafunc-
tion;ifyougettotheendofafunctionwithouthittingareturnstatement,itreturns
None. Another common cause is using the result from a list method, like sort, that
returnsNone.
IndexError: The index you are using to access a list, string, or tuple is greater than its
lengthminusone. Immediatelybeforethesiteoftheerror,addaprintstatementto
displaythevalueoftheindexandthelengthofthearray. Isthearraytherightsize?
Istheindextherightvalue?
ThePythondebugger(pdb)isusefulfortrackingdownexceptionsbecauseitallowsyouto
examinethestateoftheprogramimmediatelybeforetheerror. Youcanreadaboutpdbat
https://docs.python.org/3/library/pdb.html.
A.2.4 IaddedsomanyprintstatementsIgetinundatedwithoutput.
One of the problems with using print statements for debugging is that you can end up
buried in output. There are two ways to proceed: simplify the output or simplify the
program.

198 AppendixA. Debugging
Tosimplifytheoutput,youcanremoveorcommentoutprintstatementsthataren’thelp-
ing,orcombinethem,orformattheoutputsoitiseasiertounderstand.
Tosimplifytheprogram,thereareseveralthingsyoucando.First,scaledowntheproblem
theprogramisworkingon. Forexample, ifyouaresearchingalist, searchasmalllist. If
theprogramtakesinputfromtheuser,giveitthesimplestinputthatcausestheproblem.
Second, clean up the program. Remove dead code and reorganize the program to make
itaseasytoreadaspossible. Forexample, ifyoususpectthattheproblemisinadeeply
nestedpartoftheprogram,tryrewritingthatpartwithsimplerstructure. Ifyoususpecta
largefunction,trysplittingitintosmallerfunctionsandtestingthemseparately.
Often the process of finding the minimal test case leads you to the bug. If you find that
a program works in one situation but not in another, that gives you a clue about what is
goingon.
Similarly, rewriting a piece of code can help you find subtle bugs. If you make a change
thatyouthinkshouldn’taffecttheprogram,anditdoes,thatcantipyouoff.
A.3 Semantic errors
Insomeways, semanticerrorsarethehardesttodebug, becausetheinterpreterprovides
noinformationaboutwhatiswrong. Onlyyouknowwhattheprogramissupposedtodo.
Thefirststepistomakeaconnectionbetweentheprogramtextandthebehavioryouare
seeing. Youneedahypothesisaboutwhattheprogramisactuallydoing. Oneofthethings
thatmakesthathardisthatcomputersrunsofast.
You will often wish that you could slow the program down to human speed, and with
somedebuggersyoucan.Butthetimeittakestoinsertafewwell-placedprintstatements
is often short compared to setting up the debugger, inserting and removing breakpoints,
and“stepping”theprogramtowheretheerrorisoccurring.
A.3.1 Myprogramdoesn’twork.
Youshouldaskyourselfthesequestions:
• Is there something the program was supposed to do but which doesn’t seem to be
happening? Findthesectionofthecodethatperformsthatfunctionandmakesure
itisexecutingwhenyouthinkitshould.
• Is something happening that shouldn’t? Find code in your program that performs
thatfunctionandseeifitisexecutingwhenitshouldn’t.
• Isasectionofcodeproducinganeffectthatisnotwhatyouexpected?Makesurethat
youunderstandthecodeinquestion,especiallyifitinvolvesfunctionsormethodsin
otherPythonmodules. Readthedocumentationforthefunctionsyoucall. Trythem
outbywritingsimpletestcasesandcheckingtheresults.

A.3. Semanticerrors 199
In order to program, you need a mental model of how programs work. If you write a
programthatdoesn’tdowhatyouexpect,oftentheproblemisnotintheprogram; it’sin
yourmentalmodel.
The best way to correct your mental model is to break the program into its components
(usually the functions and methods) and test each component independently. Once you
findthediscrepancybetweenyourmodelandreality,youcansolvetheproblem.
Of course, you should be building and testing components as you develop the program.
Ifyouencounteraproblem, thereshouldbeonlyasmallamountofnewcodethatisnot
knowntobecorrect.
A.3.2 I’vegotabighairyexpressionanditdoesn’tdowhatIexpect.
Writing complex expressions is fine as long as they are readable, but they can be hard to
debug. Itisoftenagoodideatobreakacomplexexpressionintoaseriesofassignmentsto
temporaryvariables.
Forexample:
self.hands[i].addCard(self.hands[self.findNeighbor(i)].popCard())
Thiscanberewrittenas:
neighbor = self.findNeighbor(i)
pickedCard = self.hands[neighbor].popCard()
self.hands[i].addCard(pickedCard)
Theexplicitversioniseasiertoreadbecausethevariablenamesprovideadditionaldocu-
mentation, and it is easier to debug because you can check the types of the intermediate
variablesanddisplaytheirvalues.
Another problem that can occur with big expressions is that the order of evaluation may
notbewhatyouexpect. Forexample,ifyouaretranslatingtheexpression x intoPython,
2π
youmightwrite:
y = x / 2 * math.pi
Thatisnotcorrectbecausemultiplicationanddivisionhavethesameprecedenceandare
evaluatedfromlefttoright. Sothisexpressioncomputesxπ/2.
A good way to debug expressions is to add parentheses to make the order of evaluation
explicit:
y = x / (2 * math.pi)
Wheneveryouarenotsureoftheorderofevaluation,useparentheses. Notonlywillthe
programbecorrect(inthesenseofdoingwhatyouintended),itwillalsobemorereadable
forotherpeoplewhohaven’tmemorizedtheorderofoperations.
A.3.3 I’vegotafunctionthatdoesn’treturnwhatIexpect.
If you have a return statement with a complex expression, you don’t have a chance to
print the resultbefore returning. Again, you can use a temporaryvariable. For example,
insteadof:
return self.hands[i].removeMatches()

200 AppendixA. Debugging
youcouldwrite:
count = self.hands[i].removeMatches()
return count
Nowyouhavetheopportunitytodisplaythevalueofcountbeforereturning.
A.3.4 I’mreally,reallystuckandIneedhelp.
First,trygettingawayfromthecomputerforafewminutes. Computersemitwavesthat
affectthebrain,causingthesesymptoms:
• Frustrationandrage.
• Superstitiousbeliefs(“thecomputerhatesme”)andmagicalthinking(“theprogram
onlyworkswhenIwearmyhatbackward”).
• Randomwalkprogramming(theattempttoprogrambywritingeverypossiblepro-
gramandchoosingtheonethatdoestherightthing).
Ifyoufindyourselfsufferingfromanyofthesesymptoms,getupandgoforawalk. When
youarecalm,thinkabouttheprogram. Whatisitdoing? Whataresomepossiblecauses
ofthatbehavior? Whenwasthelasttimeyouhadaworkingprogram,andwhatdidyou
donext?
Sometimes it just takes time to find a bug. I often find bugs when I am away from the
computerandletmymindwander.Someofthebestplacestofindbugsaretrains,showers,
andinbed,justbeforeyoufallasleep.
A.3.5 No,Ireallyneedhelp.
Ithappens. Eventhebestprogrammersoccasionallygetstuck. Sometimesyouworkona
programsolongthatyoucan’tseetheerror. Youneedafreshpairofeyes.
Beforeyoubringsomeoneelsein,makesureyouareprepared. Yourprogramshouldbeas
simpleaspossible,andyoushouldbeworkingonthesmallestinputthatcausestheerror.
Youshouldhaveprintstatementsintheappropriateplaces(andtheoutputtheyproduce
shouldbecomprehensible). Youshouldunderstandtheproblemwellenoughtodescribe
itconcisely.
Whenyoubringsomeoneintohelp,besuretogivethemtheinformationtheyneed:
• Ifthereisanerrormessage,whatisitandwhatpartoftheprogramdoesitindicate?
• Whatwasthelastthingyoudidbeforethiserroroccurred? Whatwerethelastlines
ofcodethatyouwrote,orwhatisthenewtestcasethatfails?
• Whathaveyoutriedsofar,andwhathaveyoulearned?
Whenyoufindthebug,takeasecondtothinkaboutwhatyoucouldhavedonetofindit
faster. Nexttimeyouseesomethingsimilar,youwillbeabletofindthebugmorequickly.
Remember,thegoalisnotjusttomaketheprogramwork.Thegoalistolearnhowtomake
theprogramwork.

Appendix B
Analysis of Algorithms
ThisappendixisaneditedexcerptfromThinkComplexity,byAllenB.Downey,
also published by O’Reilly Media (2012). When you are done with this book,
youmightwanttomoveontothatone.
Analysis of algorithms is a branch of computer science that studies the performance of
algorithms,especiallytheirruntimeandspacerequirements. Seehttp://en.wikipedia.
org/wiki/Analysis_of_algorithms.
The practical goal of algorithm analysis is to predict the performance of different algo-
rithmsinordertoguidedesigndecisions.
Duringthe2008UnitedStatesPresidentialCampaign,candidateBarackObamawasasked
toperformanimpromptuanalysiswhenhevisitedGoogle. ChiefexecutiveEricSchmidt
jokingly asked him for “the most efficient way to sort a million 32-bit integers.” Obama
hadapparentlybeentippedoff,becausehequicklyreplied,“Ithinkthebubblesortwould
bethewrongwaytogo.” Seehttp://www.youtube.com/watch?v=k4RRi_ntQc8.
This is true: bubble sort is conceptually simple but slow for large datasets. The an-
swerSchmidtwasprobablylookingforis“radixsort”(http://en.wikipedia.org/wiki/
Radix_sort)1.
The goal of algorithm analysis is to make meaningful comparisons between algorithms,
buttherearesomeproblems:
• The relative performance of the algorithms might depend on characteristics of the
hardware, so one algorithm might be faster on Machine A, another on Machine B.
Thegeneralsolutiontothisproblemistospecifyamachinemodelandanalyzethe
numberofsteps,oroperations,analgorithmrequiresunderagivenmodel.
• Relativeperformancemightdependonthedetailsofthedataset. Forexample,some
sortingalgorithmsrunfasterifthedataarealreadypartiallysorted;otheralgorithms
1Butifyougetaquestionlikethisinaninterview,Ithinkabetteransweris,“Thefastestwaytosortamillion
integersistousewhateversortfunctionisprovidedbythelanguageI’musing.Itsperformanceisgoodenough
forthevastmajorityofapplications,butifitturnedoutthatmyapplicationwastooslow,Iwoulduseaprofiler
toseewherethetimewasbeingspent. Ifitlookedlikeafastersortalgorithmwouldhaveasignificanteffecton
performance,thenIwouldlookaroundforagoodimplementationofradixsort.”

| 202 |     |     | AppendixB. | AnalysisofAlgorithms |
| --- | --- | --- | ---------- | -------------------- |
runslowerinthiscase. Acommonwaytoavoidthisproblemistoanalyzetheworst
casescenario. Itissometimesusefultoanalyzeaveragecaseperformance,butthat’s
usuallyharder,anditmightnotbeobviouswhatsetofcasestoaverageover.
• Relativeperformancealsodependsonthesizeoftheproblem. Asortingalgorithm
that is fast for small lists might be slow for long lists. The usual solution to this
problem is to express run time (or number of operations) as a function of problem
size, and group functions into categories depending on how quickly they grow as
problemsizeincreases.
Thegoodthingaboutthiskindofcomparisonisthatitlendsitselftosimpleclassification
of algorithms. For example, if I know that the run time of Algorithm A tends to be pro-
portionaltothesizeoftheinput,n,andAlgorithmBtendstobeproportionalton2,thenI
expectAtobefasterthanB,atleastforlargevaluesofn.
Thiskindofanalysiscomeswithsomecaveats,butwe’llgettothatlater.
| B.1 Order | of growth |     |     |     |
| --------- | --------- | --- | --- | --- |
Supposeyouhaveanalyzedtwoalgorithmsandexpressedtheirruntimesintermsofthe
AlgorithmAtakes100n+1stepstosolveaproblemwithsize
sizeoftheinput: n; Algo-
rithmBtakesn2+n+1steps.
Thefollowingtableshowstheruntimeofthesealgorithmsfordifferentproblemsizes:
| Input | Runtimeof  | Runtimeof  |     |     |
| ----- | ---------- | ---------- | --- | --- |
| size  | AlgorithmA | AlgorithmB |     |     |
| 10    | 1001       | 111        |     |     |
| 100   | 10001      | 10101      |     |     |
| 1000  | 100001     | 1001001    |     |     |
| 10000 | 1000001    | 100010001  |     |     |
At n = 10, AlgorithmAlooksprettybad; ittakesalmost10timeslongerthanAlgorithm
B.Butforn =100theyareaboutthesame,andforlargervaluesAismuchbetter.
Thefundamentalreasonisthatforlargevaluesofn,anyfunctionthatcontainsann2
term
willgrowfasterthanafunctionwhoseleadingtermisn.Theleadingtermisthetermwith
thehighestexponent.
ForAlgorithmA,theleadingtermhasalargecoefficient,100,whichiswhyBdoesbetter
thanAforsmalln. Butregardlessofthecoefficients,therewillalwaysbesomevalueofn
| wherean2 | >   |     |     |     |
| -------- | --- | --- | --- | --- |
bn,foranyvaluesofaandb.
Thesameargumentappliestothenon-leadingterms. EveniftheruntimeofAlgorithmA
weren+1000000,itwouldstillbebetterthanAlgorithmBforsufficientlylargen.
Ingeneral,weexpectanalgorithmwithasmallerleadingtermtobeabetteralgorithmfor
large problems, but for smaller problems, there may be a crossover point where another
algorithmisbetter. Thelocationofthecrossoverpointdependsonthedetailsofthealgo-
rithms, theinputs, andthehardware, soitisusuallyignoredforpurposesofalgorithmic
| analysis. Butthatdoesn’tmeanyoucanforgetaboutit. |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- |

B.1. Orderofgrowth 203
Iftwoalgorithmshavethesameleadingorderterm,itishardtosaywhichisbetter;again,
the answer depends on the details. So for algorithmic analysis, functions with the same
leadingtermareconsideredequivalent,eveniftheyhavedifferentcoefficients.
Anorderofgrowthisasetoffunctionswhosegrowthbehaviorisconsideredequivalent.
Forexample,2n,100nandn+1belongtothesameorderofgrowth,whichiswrittenO(n)
inBig-Ohnotationandoftencalledlinearbecauseeveryfunctioninthesetgrowslinearly
withn.
Allfunctionswiththeleadingtermn2belongtoO(n2);theyarecalledquadratic.
The following table shows some of the orders of growth that appear most commonly in
algorithmicanalysis,inincreasingorderofbadness.
| Orderof |     | Name |     |
| ------- | --- | ---- | --- |
growth
| O(1)  |                         | constant |     |
| ----- | ----------------------- | -------- | --- |
| O(log | n) logarithmic(foranyb) |          |     |
b
O(n)
linear
| O(nlog | n)  | linearithmic |     |
| ------ | --- | ------------ | --- |
b
O(n2)
quadratic
| O(n3) |                      | cubic |     |
| ----- | -------------------- | ----- | --- |
| O(cn) | exponential(foranyc) |       |     |
Forthelogarithmicterms,thebaseofthelogarithmdoesn’tmatter; changingbasesisthe
equivalentofmultiplyingbyaconstant, whichdoesn’tchangetheorderofgrowth. Sim-
ilarly,allexponentialfunctionsbelongtothesameorderofgrowthregardlessofthebase
of the exponent. Exponential functions grow very quickly, so exponential algorithms are
onlyusefulforsmallproblems.
Exercise B.1. Read the Wikipedia page on Big-Oh notation at http://en.wikipedia.org/
| wiki/Big_O_notation |     | andanswerthefollowingquestions: |     |
| ------------------- | --- | ------------------------------- | --- |
1. What is the order of growth of n3+n2? What about 1000000n3+n2? What about n3+
1000000n2?
2. Whatistheorderofgrowthof (n2+n)·(n+1)? Beforeyoustartmultiplying, remember
thatyouonlyneedtheleadingterm.
3. If f isinO(g),forsomeunspecifiedfunction g,whatcanwesayaboutaf +b,whereaand
bareconstants?
|           | areinO(g),whatcanwesayabout |                              | +         |
| --------- | --------------------------- | ---------------------------- | --------- |
| 4. If f 1 | and f 2                     |                              | f 1 f 2 ? |
| 5. If f   | isinO(g)and                 | f isinO(h),whatcanwesayabout | f + f ?   |
| 1         |                             | 2                            | 1 2       |
| 6. If f   | isinO(g)and                 | f isO(h),whatcanwesayabout   | f · f ?   |
| 1         |                             | 2                            | 1 2       |
Programmers who care about performance often find this kind of analysis hard to swal-
low. Theyhaveapoint: sometimesthecoefficientsandthenon-leadingtermsmakeareal
difference. Sometimes the details of the hardware, the programming language, and the
characteristicsoftheinputmakeabigdifference. Andforsmallproblems,orderofgrowth
isirrelevant.
But if you keep those caveats in mind, algorithmic analysis is a useful tool. At least for
large problems, the “better” algorithm is usually better, and sometimes it is much better.
Thedifferencebetweentwoalgorithmswiththesameorderofgrowthisusuallyaconstant
factor,butthedifferencebetweenagoodalgorithmandabadalgorithmisunbounded!

204 AppendixB. AnalysisofAlgorithms
B.2 Analysis of basic Python operations
In Python, most arithmetic operations are constant time; multiplication usually takes
longerthanadditionandsubtraction,anddivisiontakesevenlonger,buttheseruntimes
don’t depend on the magnitude of the operands. Very large integers are an exception; in
thatcasetheruntimeincreaseswiththenumberofdigits.
Indexing operations—reading or writing elements in a sequence or dictionary—are also
constanttime,regardlessofthesizeofthedatastructure.
A for loop that traverses a sequence or dictionary is usually linear, as long as all of the
operationsinthebodyoftheloopareconstanttime. Forexample,addinguptheelements
ofalistislinear:
total = 0
for x in t:
total += x
The built-in function sum is also linear because it does the same thing, but it tends to be
fasterbecauseitisamoreefficientimplementation;inthelanguageofalgorithmicanalysis,
ithasasmallerleadingcoefficient.
Asaruleofthumb,ifthebodyofaloopisinO(na)thenthewholeloopisinO(na+1). The
exceptionisifyoucanshowthattheloopexitsafteraconstantnumberofiterations. Ifa
looprunsktimesregardlessofn,thentheloopisinO(na),evenforlargek.
Multiplyingby k doesn’tchangetheorderofgrowth,butneitherdoesdividing. Soifthe
bodyofaloopisinO(na)anditrunsn/ktimes,theloopisinO(na+1),evenforlargek.
Most string and tuple operations are linear, except indexing and len, which are constant
time. The built-in functions min and max are linear. The run-time of a slice operation is
proportionaltothelengthoftheoutput,butindependentofthesizeoftheinput.
String concatenation is linear; the run time depends on the sum of the lengths of the
operands.
Allstringmethodsarelinear,butifthelengthsofthestringsareboundedbyaconstant—
for example, operations on single characters—they are considered constant time. The
stringmethodjoinislinear;theruntimedependsonthetotallengthofthestrings.
Mostlistmethodsarelinear,buttherearesomeexceptions:
• Adding an element to the end of a list is constant time on average; when it runs
out of room it occasionally gets copied to a bigger location, but the total time for n
operationsisO(n),sotheaveragetimeforeachoperationisO(1).
• Removinganelementfromtheendofalistisconstanttime.
• SortingisO(nlogn).
Mostdictionaryoperationsandmethodsareconstanttime,buttherearesomeexceptions:
• The run time of update is proportional to the size of the dictionary passed as a pa-
rameter,notthedictionarybeingupdated.
• keys, values and items are constant time because they return iterators. But if you
loopthroughtheiterators,theloopwillbelinear.

B.3. Analysisofsearchalgorithms 205
Theperformanceofdictionariesisoneoftheminormiraclesofcomputerscience. Wewill
seehowtheyworkinSectionB.4.
ExerciseB.2. ReadtheWikipediapageonsortingalgorithmsathttp://en.wikipedia.org/
wiki/Sorting_algorithm andanswerthefollowingquestions:
1. Whatisa“comparisonsort?” Whatisthebestworst-caseorderofgrowthforacomparison
sort? Whatisthebestworst-caseorderofgrowthforanysortalgorithm?
2. Whatistheorderofgrowthofbubblesort,andwhydoesBarackObamathinkitis“thewrong
waytogo?”
3. Whatistheorderofgrowthofradixsort? Whatpreconditionsdoweneedtouseit?
4. Whatisastablesortandwhymightitmatterinpractice?
5. Whatistheworstsortingalgorithm(thathasaname)?
6. WhatsortalgorithmdoestheClibraryuse? WhatsortalgorithmdoesPythonuse? Arethese
algorithmsstable? YoumighthavetoGooglearoundtofindtheseanswers.
7. Manyofthenon-comparisonsortsarelinear,sowhydoesPythonuseanO(nlogn)compar-
isonsort?
B.3 Analysis of search algorithms
Asearchisanalgorithmthattakesacollectionandatargetitemanddetermineswhether
thetargetisinthecollection,oftenreturningtheindexofthetarget.
Thesimplestsearchalgorithmisa“linearsearch”,whichtraversestheitemsofthecollec-
tion in order, stopping if it finds the target. In the worst case it has to traverse the entire
collection,sotheruntimeislinear.
The in operator for sequences uses a linear search; so do string methods like find and
count.
If the elements of the sequence are in order, you can use a bisection search, which is
O(logn). Bisection search is similar to the algorithm you might use to look a word up
in a dictionary (a paper dictionary, not the data structure). Instead of starting at the be-
ginningandcheckingeachiteminorder,youstartwiththeiteminthemiddleandcheck
whether the word you are looking for comes before or after. If it comes before, then you
searchthefirsthalfofthesequence. Otherwiseyousearchthesecondhalf. Eitherway,you
cutthenumberofremainingitemsinhalf.
Ifthesequencehas1,000,000items,itwilltakeabout20stepstofindthewordorconclude
thatit’snotthere. Sothat’sabout50,000timesfasterthanalinearsearch.
Bisectionsearchcanbemuchfasterthanlinearsearch,butitrequiresthesequencetobein
order,whichmightrequireextrawork.
There is another data structure, called a hashtable that is even faster—it can do a search
in constant time—and it doesn’t require the items to be sorted. Python dictionaries are
implementedusinghashtables,whichiswhymostdictionaryoperations,includingthein
operator,areconstanttime.

206 AppendixB. AnalysisofAlgorithms
B.4 Hashtables
Toexplainhowhashtablesworkandwhytheirperformanceissogood,Istartwithasimple
implementationofamapandgraduallyimproveituntilit’sahashtable.
I use Python to demonstrate these implementations, but in real life you wouldn’t write
codelikethisinPython;youwouldjustuseadictionary!Sofortherestofthischapter,you
havetoimaginethatdictionariesdon’texistandyouwanttoimplementadatastructure
thatmapsfromkeystovalues. Theoperationsyouhavetoimplementare:
add(k, v): Addanewitemthatmapsfromkeyktovaluev. WithaPythondictionary,d,
thisoperationiswrittend[k] = v.
get(k): Lookupandreturnthevaluethatcorrespondstokeyk.WithaPythondictionary,
d,thisoperationiswrittend[k]ord.get(k).
For now, I assume that each key only appears once. The simplest implementation of this
interfaceusesalistoftuples,whereeachtupleisakey-valuepair.
class LinearMap:
def __init__(self):
self.items = []
def add(self, k, v):
self.items.append((k, v))
def get(self, k):
for key, val in self.items:
if key == k:
return val
raise KeyError
addappendsakey-valuetupletothelistofitems,whichtakesconstanttime.
getusesaforlooptosearchthelist: ifitfindsthetargetkeyitreturnsthecorresponding
value;otherwiseitraisesaKeyError. Sogetislinear.
Analternativeistokeepthelistsortedbykey.Thengetcoulduseabisectionsearch,which
isO(logn).Butinsertinganewiteminthemiddleofalistislinear,sothismightnotbethe
best option. There are other data structures that can implement add and get in log time,
butthat’sstillnotasgoodasconstanttime,solet’smoveon.
One way to improve LinearMap is to break the list of key-value pairs into smaller lists.
Here’s an implementation called BetterMap, which is a list of 100 LinearMaps. As we’ll
see in a second, the order of growth for get is still linear, but BetterMap is a step on the
pathtowardhashtables:
class BetterMap:
def __init__(self, n=100):
self.maps = []
for i in range(n):
self.maps.append(LinearMap())

B.4. Hashtables 207
def find_map(self, k):
index = hash(k) % len(self.maps)
return self.maps[index]
def add(self, k, v):
m = self.find_map(k)
m.add(k, v)
def get(self, k):
m = self.find_map(k)
return m.get(k)
__init__makesalistofnLinearMaps.
find_mapisusedbyaddandgettofigureoutwhichmaptoputthenewitemin,orwhich
maptosearch.
find_mapusesthebuilt-infunctionhash,whichtakesalmostanyPythonobjectandreturns
an integer. A limitation of this implementation is that it only works with hashable keys.
Mutabletypeslikelistsanddictionariesareunhashable.
Hashable objects that are considered equivalent return the same hash value, but the con-
verse is not necessarily true: two objects with different values can return the same hash
value.
find_map uses the modulus operator to wrap the hash values into the range from 0 to
len(self.maps),sotheresultisalegalindexintothelist. Ofcourse,thismeansthatmany
differenthashvalueswillwrapontothesameindex.Butifthehashfunctionspreadsthings
outprettyevenly(whichiswhathashfunctionsaredesignedtodo),thenweexpectn/100
itemsperLinearMap.
Since the run time of LinearMap.get is proportional to the number of items, we expect
BetterMaptobeabout100timesfasterthanLinearMap. Theorderofgrowthisstilllinear,
buttheleadingcoefficientissmaller. That’snice,butstillnotasgoodasahashtable.
Here(finally)isthecrucialideathatmakeshashtablesfast: ifyoucankeepthemaximum
lengthoftheLinearMapsbounded,LinearMap.getisconstanttime. Allyouhavetodois
keeptrackofthenumberofitemsandwhenthenumberofitemsperLinearMapexceeds
athreshold,resizethehashtablebyaddingmoreLinearMaps.
Hereisanimplementationofahashtable:
class HashMap:
def __init__(self):
self.maps = BetterMap(2)
self.num = 0
def get(self, k):
return self.maps.get(k)
def add(self, k, v):
if self.num == len(self.maps.maps):

208 AppendixB. AnalysisofAlgorithms
self.resize()
self.maps.add(k, v)
self.num += 1
def resize(self):
new_maps = BetterMap(self.num * 2)
for m in self.maps.maps:
for k, v in m.items:
new_maps.add(k, v)
self.maps = new_maps
__init__createsaBetterMapandinitializesnum,whichkeepstrackofthenumberofitems.
getjustdispatchestoBetterMap. Therealworkhappensinadd,whichchecksthenumber
ofitemsandthesizeoftheBetterMap: iftheyareequal,theaveragenumberofitemsper
LinearMapis1,soitcallsresize.
resizemakesanewBetterMap,twiceasbigasthepreviousone,andthen“rehashes”the
itemsfromtheoldmaptothenew.
RehashingisnecessarybecausechangingthenumberofLinearMapschangesthedenomi-
natorofthemodulusoperatorinfind_map.Thatmeansthatsomeobjectsthatusedtohash
intothesameLinearMapwillgetsplitup(whichiswhatwewanted,right?).
Rehashingislinear, soresizeislinear, whichmightseembad, sinceIpromisedthatadd
wouldbeconstanttime. Butrememberthatwedon’thavetoresizeeverytime, soaddis
usuallyconstanttimeandonlyoccasionallylinear. Thetotalamountofworktorunaddn
timesisproportionalton,sotheaveragetimeofeachaddisconstanttime!
To see how this works, think about starting with an empty HashTable and adding a se-
quence of items. We start with 2 LinearMaps, so the first 2 adds are fast (no resizing re-
quired). Let’ssaythattheytakeoneunitofworkeach. Thenextaddrequiresaresize,so
wehavetorehashthefirsttwoitems(let’scallthat2moreunitsofwork)andthenaddthe
thirditem(onemoreunit). Addingthenextitemcosts1unit,sothetotalsofaris6units
ofworkfor4items.
Thenextaddcosts5units,butthenextthreeareonlyoneuniteach,sothetotalis14units
forthefirst8adds.
Thenextaddcosts9units,butthenwecanadd7morebeforethenextresize,sothetotalis
30unitsforthefirst16adds.
After32adds,thetotalcostis62units,andIhopeyouarestartingtoseeapattern. Aftern
adds,wherenisapoweroftwo,thetotalcostis2n−2units,sotheaverageworkperadd
isalittlelessthan2units.Whennisapoweroftwo,that’sthebestcase;forothervaluesof
ntheaverageworkisalittlehigher,butthat’snotimportant. Theimportantthingisthatit
isO(1).
Figure B.1 shows how this works graphically. Each block represents a unit of work. The
columnsshowthetotalworkforeachaddinorderfromlefttoright:thefirsttwoaddscost
1uniteach,thethirdcosts3units,etc.

B.5. Glossary 209
FigureB.1: Thecostofahashtableadd.
Theextraworkofrehashingappearsasasequenceofincreasinglytalltowerswithincreas-
ingspacebetweenthem. Nowifyouknockoverthetowers,spreadingthecostofresizing
overalladds,youcanseegraphicallythatthetotalcostafternaddsis2n−2.
An important feature of this algorithm is that when we resize the HashTable it grows
geometrically; that is, we multiply the size by a constant. If you increase the size
arithmetically—addingafixednumbereachtime—theaveragetimeperaddislinear.
You can download my implementation of HashMap from https://thinkpython.com/
code/Map.py,butrememberthatthereisnoreasontouseit;ifyouwantamap,justusea
Pythondictionary.
B.5 Glossary
analysisofalgorithms: A way to compare algorithms in terms of their run time and/or
spacerequirements.
machinemodel: Asimplifiedrepresentationofacomputerusedtodescribealgorithms.
worstcase: The input that makes a given algorithm run slowest (or require the most
space).
leadingterm: Inapolynomial,thetermwiththehighestexponent.
crossoverpoint: The problem size where two algorithms require the same run time or
space.
orderofgrowth: Asetoffunctionsthatallgrowinawayconsideredequivalentforpur-
posesofanalysisofalgorithms. Forexample,allfunctionsthatgrowlinearlybelong
tothesameorderofgrowth.
Big-Ohnotation: Notationforrepresentinganorderofgrowth;forexample,O(n)repre-
sentsthesetoffunctionsthatgrowlinearly.
linear: An algorithm whose run time is proportional to problem size, at least for large
problemsizes.
quadratic: An algorithm whose run time is proportional to n2, where n is a measure of
problemsize.
search: The problem of locating an element of a collection (like a list or dictionary) or
determiningthatitisnotpresent.

| 210 | AppendixB. | AnalysisofAlgorithms |
| --- | ---------- | -------------------- |
hashtable: A data structure that represents a collection of key-value pairs and performs
searchinconstanttime.

Index
abecedarian,73,84 augmented,93,100
absfunction,52 item,74,90,116
absolutepath,139,145 tuple,116,117,119,122
access,90 assignmentstatement,9
accumulator,100 attribute,153,169
histogram,127 __dict__,168
list,93 class,172,180
string,175 initializing,168
sum,93 instance,148,153,172,180
Ackermannfunction,61,113 AttributeError,152,197
addmethod,165 augmentedassignment,93,100
additionwithcarrying,68 Austen,Jane,127
algorithm,67,69,130,201 averagecase,202
MD5,146 averagecost,208
squareroot,69
aliasing,95,96,100,149,151,170 badness,203
copyingtoavoid,99 basecase,44,47
all,186 benchmarking,133,134
alphabet,37 BetterMap,206
alternativeexecution,41 big,hairyexpression,199
ambiguity,5 Big-Ohnotation,209
anagram,101 big-ohnotation,203
anagramset,123,145 binarysearch,101
analysisofalgorithms,201,209 bingo,123
analysisofprimitives,204 birthday,160
andoperator,40 birthdayparadox,101
any,185 bisectmodule,101
appendmethod,92,97,101,174,175 bisectionsearch,101,205
arcfunction,31 bisection,debuggingby,68
Archimedianspiral,38 bitwiseoperator,3
argument,17,19,21,22,26,97 body,19,26,65
gather,118 booltype,40
keyword,33,36,191 booleanexpression,40,47
list,97 booleanfunction,54
optional,76,79,95,107,184 booleanoperator,76
positional,164,169,190 borrowing,subtractionwith,68,159
variable-lengthtuple,118 bounded,207
argumentscatter,118 bracket
arithmeticoperator,3 squiggly,103
assertstatement,159,160 bracketoperator,71,90,116
assignment,14,63,89 branch,41,47

| 212                                            |                |     | Index |
| ---------------------------------------------- | -------------- | --- | ----- |
| breakstatement,66 compoundstatement,41,47      |                |     |       |
| bubblesort,201 concatenation,12,14,22,73,74,95 |                |     |       |
| bug,6,7,13                                     | list,91,97,101 |     |       |
| worst,170 condition,41,47,65,196               |                |     |       |
| built-infunction conditional,194               |                |     |       |
| any,185,186                                    | chained,41,47  |     |       |
| bytesobject,141,145                            | nested,42,47   |     |       |
conditionalexecution,41
| calculator,8,15 conditionalexpression,183,191       |          |     |     |
| --------------------------------------------------- | -------- | --- | --- |
| callgraph,109,112 conditionalstatement,41,47,55,184 |          |     |     |
| CarTalk,88,113,124 consistencycheck,111,158         |          |     |     |
| Cardclass,172 constanttime,208                      |          |     |     |
| card,playing,171 contributors,vii                   |          |     |     |
| carrying,additionwith,68,156,158 conversion         |          |     |     |
| catch,145                                           | type,17  |     |     |
| chainedconditional,41,47 copy                       |          |     |     |
| character,71                                        | deep,152 |     |     |
checksum,143,146
shallow,152
| childclass,176,180 | slice,74,92 |     |     |
| ------------------ | ----------- | --- | --- |
choicefunction,126
toavoidaliasing,99
| circlefunction,31 copymodule,151         |     |     |     |
| ---------------------------------------- | --- | --- | --- |
| circulardefinition,55 copyingobjects,151 |     |     |     |
| class,4,147,153 countmethod,79           |     |     |     |
| Card,172 Counter,187                     |     |     |     |
| child,176,180 counter,75,79,104,111      |     |     |     |
| Deck,174 countingandlooping,75           |     |     |     |
| Hand,176 CreativeCommons,vi              |     |     |     |
| Kangaroo,170 crossoverpoint,202,209      |     |     |     |
| parent,176 crosswords,83                 |     |     |     |
| Point,148,165 cumulativesum,100          |     |     |     |
Rectangle,149
| Time,155 dataencapsulation,179,181               |     |     |     |
| ------------------------------------------------ | --- | --- | --- |
| classattribute,172,180 datastructure,122,123,132 |     |     |     |
| classdefinition,147 database,141,145             |     |     |     |
| classdiagram,177,181 databaseobject,141          |     |     |     |
| classobject,148,153,190 datetimemodule,160       |     |     |     |
| closemethod,138,141,143 dbmmodule,141            |     |     |     |
| __cmp__method,173 deadcode,52,60,198             |     |     |     |
| Collatzconjecture,65 debugger(pdb),197           |     |     |     |
collections,187,188,190 debugging,6,7,13,36,46,59,77,87,98,111,
| colon,19,194                                      | 122, 133, 144,          | 152, 159, 168, | 178, |
| ------------------------------------------------- | ----------------------- | -------------- | ---- |
| comment,12,14                                     | 185,193                 |                |      |
| commutativity,12,167                              | bybisection,68          |                |      |
| comparefunction,52                                | emotionalresponse,6,200 |                |      |
| comparingalgorithms,201                           | experimental,25         |                |      |
| comparison                                        | rubberduck,134          |                |      |
| string,77                                         | superstition,200        |                |      |
| tuple,116,174 deck,171                            |                         |                |      |
| comparisonsort,205 Deckclass,174                  |                         |                |      |
| composition,19,22,26,54,174 deck,playingcards,174 |                         |                |      |

Index 213
declaration,110,112 walk,140
decrement,64,69 working,139
deepcopy,152,153 dispatch
deepcopyfunction,152 type-based,167
defkeyword,19 dispatch,type-based,166
defaultvalue,129,134,165 divisibility,39
avoidingmutable,170 division
defaultdict,188 floating-point,39
definition floor,39,46,47
circular,55 divmod,117,158
class,147 docstring,35,37,148
function,19 dotnotation,18,26,76,148,162,172
recursive,124 DoubleDay,160
deloperator,94 doubleletters,88
deletion,elementoflist,94 Doyle,ArthurConan,25
delimiter,95,100 duplicate,101,113,146,187
designeddevelopment,160
deterministic,126,134 element,89,100
developmentplan,36 elementdeletion,94
dataencapsulation,179,181 elifkeyword,42
designed,158 Elkner,Jeff,v,vi
encapsulationandgeneralization,35 ellipses,19
incremental,52,193 elsekeyword,41
prototypeandpatch,156,158 emailaddress,117
randomwalkprogramming,134,200 embeddedobject,150,153,170
reduction,85,87 copying,152
diagram emotionaldebugging,6,200
callgraph,112 emptylist,89
class,177,181 emptystring,79,95
object,148,150,152,153,155,173 encapsulation,32,36,54,69,75,177
stack,23,97 encode,171,180
state,9,63,78,90,96,108,120,148,150, encrypt,171
152,155,173 endoflinecharacter,144
__dict__attribute,168 enumeratefunction,119
dictfunction,103 enumerateobject,119
dictionary,103,112,120,197 epsilon,67
initialize,120 equalityandassignment,63
invert,107 equivalence,96,152
lookup,106 equivalent,100
loopingwith,106 error
reverselookup,106 runtime,13,44,46,193
subtraction,129 semantic,13,193,198
traversal,120,168 shape,122
dictionarymethods,204 syntax,13,193
dbmmodule,141 errorchecking,58
dictionarysubtraction,186 errormessage,7,13,193
diff,146 evalfunction,69
Dijkstra,Edsger,87 evaluate,10
dirfunction,197 exception,13,14,193,196
directory,139,145 AttributeError,152,197

214 Index
FileNotFoundError,140 forloop,30,44,72,91,119,184
IndexError,72,78,90,197 formallanguage,4,7
KeyError,104,197 formatoperator,138,145,197
LookupError,107 formatsequence,138,145
NameError,22,197 formatstring,138,145
OverflowError,46 frame,23,26,44,56,109
RuntimeError,45 FreeDocumentationLicense,GNU,v,vi
StopIteration,185 frequency,105
SyntaxError,19 letter,123
TypeError,72,74,108,116,118,139,164, word,125,134
197 fruitfulfunction,24,26
UnboundLocalError,110 frustration,200
ValueError,46,117 function,3,17,19,25,161
exception,catching,140 abs,52
execute,11,14 ack,61,113
existsfunction,139 arc,31
experimentaldebugging,25,134 choice,126
exponent,202 circle,31
exponentialgrowth,203 compare,52
expression,10,14 deepcopy,152
bigandhairy,199 dict,103
boolean,40,47 dir,197
conditional,183,191 enumerate,119
generator,185,186,191 eval,69
extendmethod,92 exists,139
factorial,56,183
factorial,183 fibonacci,57,109
factorialfunction,56,58 find,74
factory,191 float,17
factoryfunction,188,189 fruitful,24
Falsespecialvalue,40 getattr,168
Fermat’sLastTheorem,48 getcwd,139
fibonaccifunction,57,109 hasattr,153,168
file,137 input,45
permission,140 int,17
readingandwriting,137 isinstance,58,153,166
fileobject,83,87 len,26,72,104
filename,139 list,94
FileNotFoundError,140 log,18
filterpattern,93,100,184 math,18
findfunction,74 max,117,118
flag,110,112 min,117,118
floatfunction,17 open,83,84,137,140,141
floattype,4 polygon,31
floating-point,4,7,67,183 popen,142
floating-pointdivision,39 programmerdefined,22,129
floordivision,39,46,47 randint,101,126
flowofexecution,21,26,58,59,65,178,196 random,126
flower,37 reasonsfor,24
folder,139 recursive,43

Index 215
reload,144,195 hashable,108,112,120
repr,144 HashMap,207
reversed,121 hashtable,112,206,210
shuffle,175 header,19,25,194
sorted,99,106,121 Hello,World,3
sqrt,18,53 hexadecimal,148
str,18 high-levellanguage,6
sum,118,185 histogram,105
trigonometric,18 randomchoice,126,130
tuple,115 wordfrequencies,127
tupleasreturnvalue,117 Holmes,Sherlock,25
type,153 homophone,113
void,24 hypotenuse,54
zip,118
functionargument,21 identical,100
functioncall,17,26 identity,96,152
functioncomposition,54 ifstatement,41
functiondefinition,19,20,25 immutability,74,79,97,108,115,121
functionframe,23,26,44,56,109 implementation,105,112,132,169
functionobject,27 importstatement,26,144
functionparameter,21
inoperator,205
functionsyntax,162 inoperator,76,85,90,104
functiontype,20 increment,64,69,157,163
modifier,157 incrementaldevelopment,60,193
pure,156 indentation,19,162,194
functionalprogrammingstyle,158,160 index,71,78,79,90,103,197
loopingwith,86,91
gammafunction,58 negative,72
gather,118,123,190 slice,73,91
GCD(greatestcommondivisor),61 startingatzero,71,90
generalization,32,36,85,159 IndexError,72,78,90,197
generatorexpression,185,186,191 indexing,204
generatorobject,185 infiniteloop,65,69,195,196
geometricresizing,209 infiniterecursion,44,47,58,195,196
getmethod,105 inheritance,176,178,180,190
getattrfunction,168 initmethod,164,168,172,174,176
getcwdfunction,139 initialization
globalstatement,110,112 variable,69
globalvariable,110,112 initialization(beforeupdate),64
update,110 inputfunction,45
GNUFreeDocumentationLicense,v,vi instance,148,153
greatestcommondivisor(GCD),61 asargument,149
grid,27 asreturnvalue,150
guardianpattern,59,60,78 instanceattribute,148,153,172,180
instantiate,153
Handclass,176 instantiation,148
hanging,195 intfunction,17
HAS-Arelationship,177,180 inttype,4
hasattrfunction,153,168 integer,4,7
hashfunction,108,112,207 interactivemode,11,14,24

216 Index
interface,33,36,169,179 Liskovsubstitutionprinciple,179
interlockingwords,101 list,89,94,100,121,184
interpret,6 asargument,97
interpreter,2 concatenation,91,97,101
invariant,159,160 copy,92
invertdictionary,107 element,90
invocation,76,79 empty,89
isoperator,95,152 function,94
IS-Arelationship,177,180 index,90
isinstancefunction,58,153,166 membership,90
item,74,79,89,103 method,92
dictionary,112 nested,89,91
itemassignment,74,90,116 ofobjects,174
itemupdate,91 oftuples,119
itemsmethod,120 operation,91
iteration,64,69 repetition,91
iterator,119–121,123,204 slice,91
traversal,91
join,204
listcomprehension,184,191
joinmethod,95,175
listmethods,204
literalness,5
Kangarooclass,170
localvariable,22,26
key,103,112
logfunction,18
key-valuepair,103,112,120
logarithm,135
keyboardinput,45
logarithmicgrowth,203
KeyError,104,197
KeyError,206 logicaloperator,40
lookup,112
keyword,10,14,194
lookup,dictionary,106
def,19
LookupError,107
elif,42
loop,31,36,65,119
else,41
condition,196
keywordargument,33,36,191
for,30,44,72,91
Kochcurve,49
infinite,65,196
language nested,174
formal,4 traversal,72
natural,4 while,64
safe,13 loopvariable,184
Turingcomplete,55 looping
leadingcoefficient,202 withdictionaries,106
leadingterm,202,209 withindices,86,91
leapoffaith,57 withstrings,75
lenfunction,26,72,104 loopingandcounting,75
letterfrequency,123 low-levellanguage,6
letterrotation,80,113 ls(Unixcommand),142
linear,209
lineargrowth,203 machinemodel,201,209
linearsearch,205 main,23,43,110,144
LinearMap,206 maintainable,169
Linux,25 mappattern,93,100
lipogram,84 mapto,171

Index 217
mapping,112,131 method,list,92
Markovanalysis,130 Meyers,Chris,vi
mash-up,132 minfunction,117,118
mathfunction,18 MobyProject,83
matplotlib,135 model,mental,199
maxfunction,117,118 modifier,157,160
McCloskey,Robert,73 module,18,26
md5,143 bisect,101
MD5algorithm,146 collections,187,188,190
md5sum,146 copy,151
membership datetime,160
binarysearch,101 dbm,141
bisectionsearch,101 os,139
dictionary,104 pickle,137,142
list,90 pprint,112
set,113 profile,133
memo,109,112 random,101,126,175
mentalmodel,199 reload,144,195
metaphor,methodinvocation,163 shelve,142
metathesis,123 string,125
method,36,75,161,169 structshape,122
__cmp__,173 time,101
__str__,165,174 moduleobject,18,143
add,165 module,writing,143
append,92,97,101,174,175 modulusoperator,39,47
close,138,141,143 MontyPythonandtheHolyGrail,156
count,79 MP3,146
extend,92 mromethod,179
get,105 multilinestring,35,194
init,164,172,174,176 multiplicity(inclassdiagram),178,181
items,120 multiset,187
join,95,175 mutability,74,90,92,96,111,115,121,151
mro,179 mutableobject,asdefaultvalue,170
pop,94,175
radd,167 namebuilt-invariable,144
read,143 namedtuple,190
readline,83,143 NameError,22,197
remove,94 NaN,183
replace,125 naturallanguage,4,7
setdefault,113 negativeindex,72
sort,92,99,176 nestedconditional,42,47
split,95,117 nestedlist,89,91,100
string,79 newline,45,175
strip,84,125 Newton’smethod,66
translate,125 Nonespecialvalue,24,26,52,92,94
update,120 NoneTypetype,24
values,104 notoperator,40
void,92 number,random,126
methodresolutionorder,179
methodsyntax,162 Obama,Barack,201

218 Index
object,74,79,95,96,100 oroperator,40
bytes,141,145 orderofgrowth,202,209
class,147,148,153,190 orderofoperations,11,14,199
copying,151 osmodule,139
Counter,187 other(parametername),164
database,141 OverflowError,46
defaultdict,188 overloading,169
embedded,150,153,170 override,129,134,165,173,176,179
enumerate,119
file,83,87 palindrome,61,80,86,88
function,27 parameter,21,23,26,97
generator,185 gather,118
module,143 optional,129,165
mutable,151 other,164
namedtuple,190 self,163
pipe,145 parentclass,176,180
printing,162 parentheses
set,186 argumentin,17
zip,123 empty,19,76
objectdiagram,148,150,152,153,155,173 parametersin,21,22
object-orienteddesign,169 parentclassin,176
object-orientedlanguage,169 tuplesin,115
object-orientedprogramming,147,161,169, parse,5,7
176 passstatement,41
odometer,88 path,139,145
OlinCollege,v absolute,139
openfunction,83,84,137,140,141 relative,139
operand,14 pattern
operator,7 filter,93,100,184
and,40 guardian,59,60,78
arithmetic,3 map,93,100
bitwise,3 reduce,93,100
boolean,76 search,75,79,85,107,186
bracket,71,90,116 swap,116
del,94 pdb(Pythondebugger),197
format,138,145,197 PEMDAS,11
in,76,85,90,104 permission,file,140
is,95,152 persistence,137,145
logical,40 pi,18,70
modulus,39,47 picklemodule,137,142
not,40 pickling,142
or,40 pie,37
overloading,169 pipe,142
relational,40,173 pipeobject,145
slice,73,79,91,98,116 plaintext,83,125
string,12 planneddevelopment,158
update,93 poetry,5
operatoroverloading,166,173 Pointclass,148,165
optionalargument,76,79,95,107,184 point,mathematical,147
optionalparameter,129,165 poker,171,181

Index 219
| polygonfunction,31             |     |     | randomwalkprogramming,134,200 |     |     |
| ------------------------------ | --- | --- | ----------------------------- | --- | --- |
| polymorphism,168,169           |     |     | rank,171                      |     |     |
| popmethod,94,175               |     |     | readmethod,143                |     |     |
| popenfunction,142              |     |     | readlinemethod,83,143         |     |     |
| portability,6                  |     |     | reassignment,63,68,90,110     |     |     |
| positionalargument,164,169,190 |     |     | Rectangleclass,149            |     |     |
| postcondition,36,59,179        |     |     | recursion,43,47,55,57         |     |     |
| pprintmodule,112               |     |     | basecase,44                   |     |     |
| precedence,199                 |     |     | infinite,44,58,196            |     |     |
| precondition,36,37,59,179      |     |     | recursivedefinition,56,124    |     |     |
| prefix,131                     |     |     | red-blacktree,206             |     |     |
| prettyprint,112                |     |     | reducepattern,93,100          |     |     |
| printfunction,3                |     |     | reducibleword,113,124         |     |     |
printstatement,3,7,165,197 reduction to a previously solved problem,
| problemsolving,1,6                |     |     |                       | 85              |                 |
| --------------------------------- | --- | --- | --------------------- | --------------- | --------------- |
| profilemodule,133                 |     |     | reduction             | to a previously | solved problem, |
| program,1,6                       |     |     |                       | 87              |                 |
| programtesting,87                 |     |     | redundancy,5          |                 |                 |
| programmer-definedfunction,22,129 |     |     | refactoring,34–36,180 |                 |                 |
reference,96,97,100
| programmer-defined            | type, 147, | 153, 155, |                            |     |     |
| ----------------------------- | ---------- | --------- | -------------------------- | --- | --- |
| 162,165,173                   |            |           | aliasing,96                |     |     |
| ProjectGutenberg,125          |            |           | rehashing,208              |     |     |
| prompt,2,6,45                 |            |           | relationaloperator,40,173  |     |     |
| prose,5                       |            |           | relativepath,139,145       |     |     |
| prototypeandpatch,156,158,160 |            |           | reloadfunction,144,195     |     |     |
| pseudorandom,126,134          |            |           | removemethod,94            |     |     |
| purefunction,156,160          |            |           | repetition,30              |     |     |
| Puzzler,88,113,124            |            |           | list,91                    |     |     |
| Pythagoreantheorem,52         |            |           | replacemethod,125          |     |     |
| Python                        |            |           | reprfunction,144           |     |     |
| running,2                     |            |           | representation,147,149,171 |     |     |
| Python2,2,3,33,40,45          |            |           | returnstatement,44,51,199  |     |     |
returnvalue,17,26,51,150
Pythoninabrowser,2
| PythonAnywhere,2 |     |     | tuple,117 |     |     |
| ---------------- | --- | --- | --------- | --- | --- |
reverselookup,112
| quadratic,209               |     |     | reverselookup,dictionary,106 |     |     |
| --------------------------- | --- | --- | ---------------------------- | --- | --- |
| quadraticgrowth,203         |     |     | reversewordpair,101          |     |     |
| quotationmark,3,4,35,74,194 |     |     | reversedfunction,121         |     |     |
rotation
| raddmethod,167 |     |     | letters,113        |     |     |
| -------------- | --- | --- | ------------------ | --- | --- |
| radian,18      |     |     | rotation,letter,80 |     |     |
radixsort,201
rubberduckdebugging,134
| rage,200 |     |     | runningpace,8,15,160 |     |     |
| -------- | --- | --- | -------------------- | --- | --- |
raisestatement,107,112,159
runningPython,2
| Ramanujan,Srinivasa,70  |     |     | runtimeerror,13,44,46,193,196 |     |     |
| ----------------------- | --- | --- | ----------------------------- | --- | --- |
| randintfunction,101,126 |     |     | RuntimeError,45,58            |     |     |
randomfunction,126
| randommodule,101,126,175 |     |     | safelanguage,13       |     |     |
| ------------------------ | --- | --- | --------------------- | --- | --- |
| randomnumber,126         |     |     | sanitycheck,111       |     |     |
| randomtext,131           |     |     | scaffolding,53,60,112 |     |     |

| 220                 |                                   |            |                  | Index |
| ------------------- | --------------------------------- | ---------- | ---------------- | ----- |
| scatter,118,123,191 | squigglybracket,103               |            |                  |       |
| Schmidt,Eric,201    | stablesort,205                    |            |                  |       |
| Scrabble,123        | stackdiagram,23,26,37,44,56,60,97 |            |                  |       |
| script,11,14        | state diagram,                    | 9, 14, 63, | 78, 90, 96, 108, | 120,  |
| scriptmode,11,14,24 | 148,150,152,155,173               |            |                  |       |
| search,107,205,209  | statement,10,14                   |            |                  |       |
assert,159,160
searchpattern,75,79,85,186
| search,binary,101              | assignment,9,63              |     |     |     |
| ------------------------------ | ---------------------------- | --- | --- | --- |
| search,bisection,101           | break,66                     |     |     |     |
| self(parametername),163        | compound,41                  |     |     |     |
| semanticerror,13,14,193,198    | conditional,41,47,55,184     |     |     |     |
| semantics,14,162               | for,30,72,91                 |     |     |     |
| sequence,4,71,79,89,94,115,121 | global,110,112               |     |     |     |
| set,130,186                    | if,41                        |     |     |     |
| anagram,123,145                | import,26,144                |     |     |     |
| setmembership,113              | pass,41                      |     |     |     |
| setsubtraction,186             | print,3,7,165,197            |     |     |     |
| setdefault,189                 | raise,107,112,159            |     |     |     |
| setdefaultmethod,113           | return,44,51,199             |     |     |     |
| sexagesimal,158                | try,140,153                  |     |     |     |
| shallowcopy,152,153            | while,64                     |     |     |     |
| shape,123                      | stepsize,79                  |     |     |     |
| shapeerror,122                 | StopIteration,185            |     |     |     |
| shell,142,145                  | strfunction,18               |     |     |     |
| shelvemodule,142               | __str__method,165,174        |     |     |     |
| shufflefunction,175            | string,4,7,94,121            |     |     |     |
| sinefunction,18                | accumulator,175              |     |     |     |
| singleton,108,112,115          | comparison,77                |     |     |     |
| slice,79                       | empty,95                     |     |     |     |
| copy,74,92                     | immutable,74                 |     |     |     |
| list,91                        | method,75                    |     |     |     |
| string,73                      | multiline,35,194             |     |     |     |
| tuple,116                      | operation,12                 |     |     |     |
| update,92                      | slice,73                     |     |     |     |
| sliceoperator,73,79,91,98,116  | triple-quoted,35             |     |     |     |
| sortmethod,92,99,176           | stringconcatenation,204      |     |     |     |
| sorted                         | stringmethod,79              |     |     |     |
| function,99,106                | stringmethods,204            |     |     |     |
| sortedfunction,121             | stringmodule,125             |     |     |     |
| sorting,204,205                | stringrepresentation,144,165 |     |     |     |
| specialcase,87,157             | stringtype,4                 |     |     |     |
| specialvalue                   | stripmethod,84,125           |     |     |     |
| False,40                       | structshapemodule,122        |     |     |     |
| None,24,26,52,92,94            | structure,5                  |     |     |     |
| True,40                        | subject,163,169              |     |     |     |
| spiral,38                      | subset,187                   |     |     |     |
| splitmethod,95,117             | subtraction                  |     |     |     |
| sqrt,53                        | dictionary,129               |     |     |     |
| sqrtfunction,18                | withborrowing,68             |     |     |     |
| squareroot,66                  | subtractionwithborrowing,159 |     |     |     |

Index 221
suffix,131 TuringThesis,55
suit,171 Turing,Alan,55
sum,185 turtlemodule,48
sumfunction,118 turtletypewriter,37
superstitiousdebugging,200 type,4,7
swappattern,116 bool,40
syntax,5,7,13,162,194 dict,103
syntaxerror,13,14,193 file,137
SyntaxError,19 float,4
function,20
temporaryvariable,51,60,199 int,4
testcase,minimal,198 list,89
testing NoneType,24
andabsenceofbugs,87 programmer-defined,147,153,155,162,
incrementaldevelopment,52 165,173
ishard,87 set,130
knowingtheanswer,53 str,4
leapoffaith,57 tuple,115
minimaltestcase,198 typechecking,58
text typeconversion,17
plain,83,125 typefunction,153
random,131 type-baseddispatch,166,167,169
textfile,145 TypeError,72,74,108,116,118,139,164,197
Timeclass,155 typewriter,turtle,37
timemodule,101 typographicalerror,134
token,5,7
traceback,24,26,44,46,107,196 UnboundLocalError,110
translatemethod,125 underscorecharacter,10
traversal,72,75,77,79,85,93,100,105,106, uniqueness,101
119,127 Unixcommand
dictionary,168 ls,142
list,91 update,64,67,69
traverse database,141
dictionary,120 globalvariable,110
triangle,48 histogram,127
trigonometricfunction,18 item,91
triple-quotedstring,35 slice,92
Truespecialvalue,40 updatemethod,120
trystatement,140,153 updateoperator,93
tuple,115,117,121,122 usebeforedef,20
askeyindictionary,120,132
assignment,116 value,4,7,95,96,112
comparison,116,174 default,129
inbrackets,120 tuple,117
singleton,115 ValueError,46,117
slice,116 valuesmethod,104
tupleassignment,117,119,122 variable,9,14
tuplefunction,115 global,110
tuplemethods,204 local,22
Turingcompletelanguage,55 temporary,51,60,199

222 Index
updating,64
variable-lengthargumenttuple,118
veneer,175,180
voidfunction,24,26
voidmethod,92
vorpal,55
walk,directory,140
whileloop,64
whitespace,46,84,144,194
wordcount,143
wordfrequency,125,134
word,reducible,113,124
workingdirectory,139
worstbug,170
worstcase,202,209
zero,indexstartingat,71
zero,indexstartingat,90
zipfunction,118
usewithdict,120
zipobject,123
Zipf’slaw,134