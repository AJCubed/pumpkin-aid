package com.pumpkin.prescreeningbe.controller;

import com.pumpkin.prescreeningbe.model.PreScreening;
import com.pumpkin.prescreeningbe.service.PreScreeningService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;

@Controller
public class PreScreeningController {
    private final PreScreeningService preScreeningService;

    @Autowired
    public PreScreeningController(PreScreeningService preScreeningService) {
        this.preScreeningService = preScreeningService;
    }

    @PostMapping("/uploadPreScreening")
    public void uploadPreScreening(@RequestBody PreScreening preScreening) {
        preScreeningService.savePreScreening(preScreening);
    }

    @GetMapping("/getPreScreening/{name}")
    public List<PreScreening> getPreScreening(String name) {
        return preScreeningService.getPreScreening(name);
    }
}
