package org.nullProject;

import org.jetbrains.annotations.NotNull;

import java.util.List;

public class InputHandler {
    private String role = null;
    private String difficulty = null;
    private String gender = null;
    private String species = null;
    private String tier = null;
    private String availability = null;
    private String organization = null;
    private String cinematic = null;
    private Integer release_year = null;
    private String release_month = null;
    private String meta = null;

    public void help(){
        System.out.println(
                """
                        Example input:
                        I'm <n> years old and I want to try playing with new characters.
                        #Optional 0
                        I like <female/male/_> <heroic/villainous/neutral/_> characters>.
                        #Optional 1
                        I like the <tank/healer/dd/_> role.
                        #Optional 2
                        I want to play something <simple/medium/difficult/_>.
                        #Optional 3
                        I want the character to be at least <d/c/b/bb/a/aa/_> tier.
                        #Optional 4
                        I want to play a character that was released before <2016/.../2023> | in <month>.
                        #Optional 5
                        I’m <interested/not interested> in the character’s story.
                        #Optional 6
                        I like <people/animals/robots/cyborgs>.
                        #Optional 7
                        I'm <ready/not ready> to spend time or money on unlocking a character.
                        
                        Who can I play on?
                        """
        );
    }

    public void handle(@NotNull List<String> data){
        System.out.println(data);
        for (String l:data) {
            String[] line = l.replace(".","").split(" ");
            if(l.matches("\\D*[0-9]{2}\\s(years)\\D*")){
                try{
                    if (Integer.parseInt(line[1]) < 12){
                        System.out.println("This game is PG12.");
                        System.exit(0);
                        System.out.println(line[1]);
                    }
                }catch (NumberFormatException e){
                    System.out.println("Can't read age.");
                }
            }
            else if(l.matches("\\D*(characters)\\D*")){
                gender = line[2];
                if(line[3].equals("heroic"))
                    organization = "overwatch";
                else if (line[3].equals("villainous")) {
                    organization = "claw";
                } else  {
                    organization = line[3];
                }
                System.out.println("gender: " + gender + "\norg: " + organization);
            }
            else if(l.matches("\\D*(role)\\D*")){
                role = line[3];
                System.out.println("role: " + role);
            }
            else if(l.matches("\\D*(something)\\D*")){
                difficulty = line[5];
                System.out.println("diff: " + difficulty);
            }
            else if(l.matches("\\D*(tier)\\D*")){
                tier = line[8];
                System.out.println("tier: " + tier);
            }
            else if(l.contains("released")){
                try {
                    release_year = Integer.valueOf(line[10]);
                }catch (NumberFormatException e){
                    System.out.println("Release year must be a number like 2016 etc.");
                    release_year = null;
                }
                if (l.length() > 57){
                    release_month = line[12];}
                System.out.println("year: " + release_year + " month: " + release_month);
            }
            else if(l.matches("\\D*(story)\\D*")){
                if (!l.contains("not interested"))
                    cinematic = "have";
                System.out.println("cinematic: "+cinematic);
            }
            else if(l.matches("\\D*(prefer)\\D*")){
                species = line[5];
                System.out.println("species: "+species);
            }
            else if(l.matches("\\D*(money)\\D*")){
                if (l.contains("not ready")){availability = "free";}
                else {availability = null;}
                System.out.println("aval.: "+ availability);
            }
            else if(l.contains("interested in meta")){
                meta = "interested";
                System.out.println("meta: "+ meta);
            }

        }

    }

    public String Meta() {
        return meta;
    }

    public String Role() {
        return role;
    }

    public String Difficulty() {
        return difficulty;
    }

    public String Gender() {
        return gender;
    }

    public String Species() {
        return species;
    }

    public String Tier() {
        return tier;
    }

    public String Availability() {
        return availability;
    }

    public String Organization() {
        return organization;
    }

    public String Cinematic() {
        return cinematic;
    }

    public Integer Release_year() {
        return release_year;
    }

    public String Release_month() {
        return release_month;
    }
}
