package com.pumpkin.prescreeningbe.service;

import com.pumpkin.prescreeningbe.model.PreScreening;
import com.pumpkin.prescreeningbe.repository.PreScreeningRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PreScreeningService {
    private final PreScreeningRepository preScreeningRepository;

    @Autowired
    public PreScreeningService(PreScreeningRepository preScreeningRepository) {
        this.preScreeningRepository = preScreeningRepository;
    }

    public void savePreScreening(PreScreening preScreening) {
        preScreeningRepository.save(preScreening);
    }

    public List<PreScreening> getPreScreening(String name) {
        List<PreScreening> preScreenings = preScreeningRepository.findAllByName(name);

        if (preScreenings == null || preScreenings.size() == 0) {
            return null;
        }

        return preScreenings;
    }
}
