package com.example.psychetest

import android.content.Intent
import android.os.Build.VERSION_CODES.O
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.ContactsContract
import android.widget.Toast
import com.example.psychetest.databinding.ActivityMainBinding
import com.example.psychetest.databinding.ActivityQuestionFiveBinding
import com.example.psychetest.databinding.ActivityQuestionSixBinding
import com.example.psychetest.databinding.ActivityQuestionTwoBinding
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import java.util.jar.Attributes

class QuestionSix : AppCompatActivity() {

    private var binding: ActivityQuestionSixBinding? = null
    private lateinit var database : DatabaseReference

    var calc = calc()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityQuestionSixBinding.inflate(layoutInflater)
        setContentView(binding?.root)

        binding?.OptA6?.setOnClickListener {
            calc = addValues(calc,30,0,15,0,20)
            navigateToQuestionTwo()
        }

        binding?.OptB6?.setOnClickListener {
            calc = addValues(calc,0,0,10,0,0)
            calc = subtractValue(calc,0,0,0,20,0)
            navigateToQuestionTwo()
        }

        binding?.OptC6?.setOnClickListener {
            calc = addValues(calc, 0,0,0,30,0)
            calc = subtractValue(calc,0,0,10,0,0)
            navigateToQuestionTwo()
        }

        binding?.OptD6?.setOnClickListener {
            calc = subtractValue(calc,20,0,0,20,0)
            navigateToQuestionTwo()
        }

        database = FirebaseDatabase.getInstance().reference.child("calc")
        val userIdentifier = "current_user_app"

        database = FirebaseDatabase.getInstance().reference.child("Oceans").child(userIdentifier)

        database.setValue(calc).addOnSuccessListener {
            Toast.makeText(this, "Answers Submitted", Toast.LENGTH_SHORT).show()
        }.addOnFailureListener {
            Toast.makeText(this, "Try Again", Toast.LENGTH_SHORT).show()
        }

    }
    private fun navigateToQuestionTwo() {
        startActivity(Intent(this, LastPage::class.java))
        finish()
    }
    fun addValues(data: calc, addition1: Int, addition2: Int, addition3: Int, addition4: Int, addition5: Int): calc {
        val newValue1 = data.O + addition1
        val newValue2 = data.C + addition2
        val newValue3 = data.E + addition3
        val newValue4 = data.A + addition4
        val newValue5 = data.N + addition5
        return data.copy(O = newValue1, C = newValue2, E = newValue3, A = newValue4, N = newValue5)
    }

    fun subtractValue(data: calc, subtraction1: Int, subtraction2: Int, subtraction3: Int, subtraction4: Int, subtraction5: Int): calc {
        val newValue1 = data.O - subtraction1
        val newValue2 = data.C - subtraction2
        val newValue3 = data.E - subtraction3
        val newValue4 = data.A - subtraction4
        val newValue5 = data.N - subtraction5
        return data.copy(O = newValue1, C = newValue2, E = newValue3, A = newValue4, N = newValue5)
    }
}