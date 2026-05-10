:- use_module(library(clpfd)).

define(Vars, Modules, Research) :- 

    Modules = [CS, Mathematics, Philosophy, History, M5],
    Research = [AI, ClimateChange, QuantumPhysics, Neuroscience, MedievalLiterature],
    Cars = [Tesla, BMW, Mercedes, Audi, Volvo],
    Universities = [Oxford, Cambridge, Harvard, MIT, Stanford],
    Decor = [Blue, Green, Red, Yellow, White],
    Drinks = [Espresso, HerbalTea, GreenTea, BlackCoffee, D5],

    append([Modules, Research, Cars, Universities, Decor, Drinks], Vars),

    Vars ins 1..5,

    all_distinct(Modules),
    all_distinct(Research),
    all_distinct(Cars),
    all_distinct(Universities),
    all_distinct(Decor),
    all_distinct(Drinks),

    CS #= Blue,
    Oxford #= Tesla,
    AI #= Espresso,
    Cambridge #= 1,
    office_next_to(BMW, Green),
    ClimateChange #= HerbalTea,
    Mathematics #= Red,
    Mercedes #= QuantumPhysics,
    GreenTea #= 3,
    office_next_to(Cambridge, Yellow),
    Volvo #= Philosophy,
    office_next_to(Neuroscience, Audi),
    History #= BlackCoffee,
    White #= MIT,
    Stanford #> Harvard.

office_next_to(O1, O2) :-
    abs(O1 - O2) #= 1.

solve_riddle_full(Professor, Vars) :-
    define(Vars, Modules, Research),
    labeling([ffc], Vars),

    Modules = [CS, Mathematics, Philosophy, History, M5],
    Research = [_, _, _, _, MedievalLiterature],

    ( MedievalLiterature =:= CS -> Professor = cs
    ; MedievalLiterature =:= Mathematics -> Professor = mathematics
    ; MedievalLiterature =:= Philosophy -> Professor = philosophy
    ; MedievalLiterature =:= History -> Professor = history
    ; MedievalLiterature =:= M5 -> Professor = module5
    ).

solve_riddle_office(Professor, MedievalOffice) :-
    define(Vars, Modules, Research),
    labeling([ffc], Vars),

    Modules = [CS, Mathematics, Philosophy, History, M5],
    Research = [_, _, _, _, MedievalLiterature],

    MedievalOffice = MedievalLiterature,

    ( MedievalLiterature =:= CS -> Professor = cs
    ; MedievalLiterature =:= Mathematics -> Professor = mathematics
    ; MedievalLiterature =:= Philosophy -> Professor = philosophy
    ; MedievalLiterature =:= History -> Professor = history
    ; MedievalLiterature =:= M5 -> Professor = module5
    ).
