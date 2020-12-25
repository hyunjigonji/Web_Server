package com.example.restfulwebservice;

// lombok dependency -> getter , setter , etc.
import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class HelloWorldBean {
    private String message;
//    public String getMessage(){
//        return this.message;
//    }
//    public void setMessage(String msg){
//        this.message = msg;
//    }
//    public HelloWorldBean(String message) {
//        this.message = message;
//    }

}
