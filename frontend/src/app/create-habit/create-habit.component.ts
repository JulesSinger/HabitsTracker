import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { HabitsService } from '../habits.service';

@Component({
  selector: 'app-create-habit',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule
  ],
  templateUrl: './create-habit.component.html',
  styleUrl: './create-habit.component.scss'
})
export class CreateHabitComponent {
  applyForm = new FormGroup({
    title: new FormControl(''),
  });

  habitService: HabitsService = inject(HabitsService);

  submitHabit() {
    this.habitService.createHabit(
      this.applyForm.value.title ?? '',
    );
  }
}
