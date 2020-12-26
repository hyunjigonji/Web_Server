package com.example.restfulwebservice.user;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

@Service
public class UserDaoService {
    private static List<User> users = new ArrayList<>();
    private static int usersCount = 3;

    static{
        users.add(new User(1, "Hyunji", new Date(), "pass1", "1111"));
        users.add(new User(2, "Eomji", new Date(), "pass2", "2222"));
        users.add(new User(3, "Brown", new Date(), "pass3", "3333"));
    }

    public List<User> findAll(){
        return users;
    }

    public User save(User user){
        if(user.getId() == null){
            user.setId(++usersCount);
        }
        users.add(user);
        return user;
    }

    public User findOne(int id){
        for(User user: users){
            if(user.getId() == id){
                return user;
            }
        }
        return null; // not found
    }

    public User deleteById(int id){
        Iterator<User> iterator = users.iterator();

        while(iterator.hasNext()){
            User user = iterator.next();

            if(user.getId() == id){
                iterator.remove();
                return user;
            }
        }
        return null; // not found
    }
}
