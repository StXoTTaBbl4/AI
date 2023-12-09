package org.nullProject;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        InputHandler inputHandler = new InputHandler();
        RequestHandler requestHandler = new RequestHandler();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input;
        ArrayList<String> results = new ArrayList<>();
        while(true){

            System.out.println("Path to file or command");
            //D:\ITMO\3\AI\Lab3\src\request.txt
            input = reader.readLine();
            switch (input) {
                case "exit":
                    System.exit(0);
                case "backup":
                    requestHandler.backup(results);
                    continue;
                case "rollback":
                    results = requestHandler.rollback();
                    continue;
                case "help":
                    inputHandler.help();
                    continue;
                case "reset":
                    inputHandler = new InputHandler();
                    continue;
            }
            inputHandler.handle(Files.readAllLines(Paths.get(input)));
            results = requestHandler.handle(inputHandler);
            if (results.isEmpty()){
                System.out.println("Quite empty, huh?");
                continue;
            }
            System.out.println("Suggested characters:");
            results.stream().iterator().forEachRemaining(System.out::println);
        }

    }

}