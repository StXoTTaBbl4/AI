package org.nullProject;

import org.jpl7.Atom;
import org.jpl7.Integer;
import org.jpl7.Query;
import org.jpl7.Term;
import org.jpl7.Variable;

import java.util.ArrayList;
import java.util.Map;

public class RequestHandler {
    private ArrayList<String> backUp = new ArrayList<>();

    public ArrayList<String> handle(InputHandler handler){

        Query facts = new Query(
                "consult",
                new Term[] {new Atom("src/facts.pl")}
        );
        Query rules = new Query(
                "consult",
                new Term[] {new Atom("src/rules.pl")}
        );
        System.out.println( "facts file connected? " + (facts.hasSolution() ? "Connected!" : "Failed!"));
        System.out.println( "rules file connected? " + (rules.hasSolution() ? "Connected!" : "Failed!"));

//        Query q2 = new Query("hero", new Term[]{new Atom("ana"), new Atom("_")});
//        System.out.println(q2.hasSolution());
        Variable X = new Variable("X");
        ArrayList<String> solutions;

        Query q = new Query("character", new Term[]{X});
        solutions = normalize(q.allSolutions());

        if (handler.Role() != null){
            System.out.println("Role===================");
            q = new Query("role", new Term[]{X, new Atom(handler.Role())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Difficulty() != null){
            System.out.println("Diff===================");
            q = new Query("difficulty",new Term[]{X,new Atom(handler.Difficulty())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if (handler.Meta() != null){
            System.out.println("Meta===================");
            q = new Query("meta_hero",new Term[]{X,new Atom(handler.Meta())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Gender() != null){
            System.out.println("Gender===================");
            q = new Query("gender",new Term[]{X,new Atom(handler.Gender())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Species() != null){
            System.out.println("Spec===================");
            q = new Query("species",new Term[]{X,new Atom(handler.Species())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Tier() != null){
            System.out.println("tier===================");
            q = new Query("tier",new Term[]{X,new Atom(handler.Tier())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Availability() != null){
            System.out.println("aval===================");
            q = new Query("availability",new Term[]{X,new Atom(handler.Availability())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Organization() != null){
            System.out.println("org===================");
            q = new Query("organization",new Term[]{X,new Atom(handler.Organization())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Cinematic() != null){
            System.out.println("Cinematic===================");
            q = new Query("have_backstory",new Term[]{X,new Atom(handler.Cinematic())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Release_year() != null){
            System.out.println("Release year===================");
            q = new Query("release_year",new Term[]{X,new Integer(handler.Release_year())});
            summary(solutions, normalize(q.allSolutions()));
        }
        if(handler.Release_month() != null){
            System.out.println("Release month===================");
            q = new Query("release_month",new Term[]{X,new Atom(handler.Release_month().trim())});
            summary(solutions, normalize(q.allSolutions()));
        }
        return solutions;
    }

    public void backup(ArrayList<String> current){
        backUp = current;
    }
    public ArrayList<String> rollback(){
        return backUp;
    }

    private ArrayList<String> normalize(Map<String, Term>[] solutions){
        ArrayList<String> res = new ArrayList<>();

        for(Map<String, Term> m: solutions) {
            res.add(m.get("X").toString());
        }
//        System.out.println("========================");
//        System.out.println(res);
        return res;
    }

    private void summary(ArrayList<String> prev, ArrayList<String> current){
        prev.removeIf(obj -> !current.contains(obj));
        System.out.println(prev);
    }
}
