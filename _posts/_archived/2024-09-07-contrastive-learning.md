---
title: Contrastive Learning Notes
tags: notes
comments: true
---

semi supervised learning 半监督学习 一小部分标记数据和大量未标记数据一起训练
self supervised learning 自监督学习 和无监督学习一样，未标记数据输入模型，模型在训练迭代中将预测到的最高置信度的标记并重新投入训练。（即渐近的自动标记）
al和SSL相反，将最不确定的数据拿出来给人类专家去标记 oracle