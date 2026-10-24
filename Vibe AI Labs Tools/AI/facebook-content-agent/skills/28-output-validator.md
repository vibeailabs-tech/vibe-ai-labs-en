# [28] Skill: output-validator

## Mục đích
Final check trước khi trả output cho user. HARD GATE — fail → bounce, không trả bài lỗi cho user.
Checklist 11 điểm bao phủ toàn bộ pipeline.

## Input
- `post_package`: toàn bộ output package từ pipeline
- `brand_voice`: context từ brand-voice-loader
- `pipeline_log`: list skill đã chạy + kết quả

## Checklist 11 điểm

Kiểm tra từng điểm — Pass (✅) hoặc Fail (❌):

```
[ ] 1. TONE MATCH
    Giọng văn khớp với brand_voice.tone?
    Check: xưng hô đúng, vocabulary phù hợp, không quá formal/casual hơn brand

[ ] 2. BANNED TERMS CLEAN
    Không có từ nào trong brand_voice.banned_terms?
    Check: scan toàn bộ bài bao gồm caption và first comment

[ ] 3. HOOK IN 3 LINES
    Hook rõ ràng và hoàn toàn nằm trong 3 dòng đầu?
    Check: dòng 3 có tạo tension/tò mò để bấm "Xem thêm" không?

[ ] 4. PILLAR ALIGNED
    Bài thuộc đúng content pillar đã chọn?
    Check: nội dung khớp với mô tả pillar trong brand_voice.pillars

[ ] 5. CTA FIT
    CTA phù hợp với goal và funnel stage?
    Check: TOFU=nhẹ, MOFU=trung, BOFU=mạnh

[ ] 6. POLICY PASSED
    fb-policy-checker đã chạy và result = pass hoặc flag_auto_fixed?
    Check: không có block_rewrite_required trong pipeline_log

[ ] 7. READABILITY FORMATTED
    fb-readability-formatter đã chạy?
    Check: có formatted_post trong package

[ ] 8. VISUAL BRIEF PRESENT
    fb-visual-brief đã tạo brief?
    Check: có visual_brief trong package với đủ concept + text_overlay + color_direction

[ ] 9. FORMAT MATCHES
    Format thực tế của bài khớp với format_decision từ fb-format-selector?
    Check: carousel phải có slides, reels phải có script beats

[ ] 10. SAVE OR SHARE THRESHOLD
    save_score ≥ 6 HOẶC share_score ≥ 6?
    Check: từ fb-save-share-optimizer output

[ ] 11. REVIEW QUEUE DECISION
    Có routing_decision từ fb-review-queue?
    Check: decision là auto hoặc approved/edited (không phải pending hoặc rejected)
```

## Kết quả

### All 11 pass → ✅ VALIDATED
Trả toàn bộ package cho user.

### Bất kỳ điểm nào fail → ❌ BOUNCE
- Xác định skill nào chịu trách nhiệm cho điểm fail
- Bounce về skill đó với context rõ ràng: "Điểm [X] fail vì [lý do] — cần [action cụ thể]"
- Ghi retry count — max 2 lần retry mỗi skill

## Output (khi pass)

```yaml
validation_result:
  status: validated
  checklist:
    tone_match: pass
    banned_terms_clean: pass
    hook_in_3_lines: pass
    pillar_aligned: pass
    cta_fit: pass
    policy_passed: pass
    readability_formatted: pass
    visual_brief_present: pass
    format_matches: pass
    save_share_threshold: pass
    review_queue_decided: pass
  score: "11/11"
  final_package:
    post_content: [bài hoàn chỉnh ready to publish]
    visual_brief: [brief cho designer]
    send_time: [top slot từ fb-send-time-optimizer]
    first_comment_plan: [từ fb-first-comment-strategy]
    confidence_score: [aggregate từ fb-review-queue]
    routing_decision: [auto / approved / edited]
    execution_log: [log toàn bộ pipeline]
```

## Output (khi fail)

```yaml
validation_result:
  status: failed
  failed_checks:
    - check: [tên check]
      reason: [lý do fail]
      bounce_to_skill: [skill cần chạy lại]
      instruction: [hướng dẫn cụ thể cho skill đó]
  retry_count: [số lần đã retry]
```
