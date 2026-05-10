:- use_module(library(clpfd)).

% Helper predicate for adjacency (next to each other)
next_to(X, Y) :- abs(X - Y) #= 1.

solve_university_puzzle(MedievalDept) :-
    % 1. Variables and Domains
    % Every variable takes a value from 1 to 5 representing the office number.
    
    Departments = [CS, Mathematics, Philosophy, History, Dept5],
    Research = [AI, ClimateChange, QuantumPhysics, Neuroscience, MedievalLiterature],
    Cars = [Tesla, BMW, Mercedes, Audi, Volvo],
    Universities = [Oxford, Cambridge, Harvard, MIT, Stanford],
    Decor = [Blue, Green, Red, Yellow, White],
    Drinks = [Espresso, HerbalTea, GreenTea, BlackCoffee, Drink51],

    % Combine all lists into one for domain setting
    append([Departments, Research, Cars, Universities, Decor, Drinks], AllVars),
    AllVars ins 1..5,

    % 2. Global Constraints: All values in each category must be unique
    all_distinct(Departments),
    all_distinct(Research),
    all_distinct(Cars),
    all_distinct(Universities),
    all_distinct(Decor),
    all_distinct(Drinks),

    % 3. Specific Constraints
    CS #= Blue,                                     % C1
    Oxford #= Tesla,                                % C2
    AI #= Espresso,                                 % C3
    Cambridge #= 1,                                 % C4
    next_to(BMW, Green),                            % C5
    ClimateChange #= HerbalTea,                     % C6
    Mathematics #= Red,                             % C7
    Mercedes #= QuantumPhysics,                     % C8
    GreenTea #= 3,                                  % C9
    next_to(Cambridge, Yellow),                     % C10
    Volvo #= Philosophy,                            % C11
    next_to(Neuroscience, Audi),                    % C12
    History #= BlackCoffee,                         % C13
    White #= MIT,                                   % C14
    Stanford #> Harvard,                            % C15

    % 4. Search for the solution
    label(AllVars),

    % 5. Identify which department matches Medieval Literature
    (MedievalLiterature #= CS -> MedievalDept = 'Computer Science' ;
     MedievalLiterature #= Mathematics -> MedievalDept = 'Mathematics' ;
     MedievalLiterature #= Philosophy -> MedievalDept = 'Philosophy' ;
     MedievalLiterature #= History -> MedievalDept = 'History' ;
     MedievalLiterature #= Dept5 -> MedievalDept = 'Dept5').

% To run this, use the query: ?- solve_university_puzzle(Result).
