package com.pumpkin.prescreeningbe.model;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;

import javax.persistence.*;
import java.io.Serial;
import java.util.List;

@Entity
@Table(name = "pre_screening")
@JsonDeserialize(builder = PreScreening.Builder.class)
public class PreScreening {
    @Serial
    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String name;
    private String birthday;
    List<String> symptoms;
    String summary;
    String department;
    String apptDate;

    public PreScreening() {}

    private PreScreening(Builder builder) {
        this.id = builder.id;
        this.name = builder.name;
        this.birthday = builder.birthday;
        this.symptoms = builder.symptoms;
        this.summary = builder.summary;
        this.apptDate = builder.apptDate;
        this.department = builder.department;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getBirthday() {
        return birthday;
    }

    public List<String> getSymptoms() {
        return symptoms;
    }

    public String getSummary() {
        return summary;
    }

    public String getApptDate() {
        return apptDate;
    }

    public String getDepartment() {
        return department;
    }

    public class Builder {
        private Long id;
        private String name;
        private String birthday;
        private List<String> symptoms;
        private String summary;
        private String department;
        private String apptDate;

        public Builder() {}

        public Builder(Long id) {
            this.id = id;
        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setBirthday(String birthday) {
            this.birthday = birthday;
            return this;
        }

        public Builder setSymptoms(List<String> symptoms) {
            this.symptoms = symptoms;
            return this;
        }

        public Builder setSummary(String summary) {
            this.summary = summary;
            return this;
        }

        public Builder setApptDate(String apptDate) {
            this.apptDate = apptDate;
            return this;
        }

        public Builder setDepartment(String department) {
            this.department = department;
            return this;
        }

        public PreScreening build() {
            return new PreScreening(this);
        }
    }
}
